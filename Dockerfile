FROM python:3.13-alpine AS builder

WORKDIR /service

COPY Pipfile Pipfile.lock ./

RUN pip install --no-cache-dir --no-input pipenv
RUN pipenv install --system --deploy

# Test
FROM builder AS test
WORKDIR /service

COPY tests ./tests
COPY app ./app
COPY tests/test.env ./.env

RUN pipenv install --system --deploy --dev
RUN python -m pytest

# Runtime
FROM python:3.13-alpine AS runtime

# Set environment variables
ARG AWS_ACCESS_KEY
ARG AWS_SECRET_KEY
ARG AWS_REGION
ARG AWS_BUCKET
ARG PROVIDER=s3
ENV AWS_ACCESS_KEY=${AWS_ACCESS_KEY}
ENV AWS_SECRET_KEY=${AWS_SECRET_KEY}
ENV AWS_REGION=${AWS_REGION}
ENV AWS_BUCKET=${AWS_BUCKET}
ENV PROVIDER=${PROVIDER}

WORKDIR /service

COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY app ./app

EXPOSE 8000

CMD ["python", "-m", "fastapi", "run", "--port", "8000"]