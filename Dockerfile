# Use a basic image
FROM python:3.13-slim

# Define working directory
WORKDIR /bucket

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files first
COPY Pipfile Pipfile.lock /bucket/

# Install pipenv globally
RUN pip install --no-cache-dir pipenv

# Install dependencies globally, without creating a virtual environment
RUN pipenv install --system --deploy

# Copy the rest of the application code
COPY . /bucket

# Expose the specified port
EXPOSE 8000

# Configuring behavior to suit the environment
CMD ["pipenv", "run", "fastapi", "run"]
