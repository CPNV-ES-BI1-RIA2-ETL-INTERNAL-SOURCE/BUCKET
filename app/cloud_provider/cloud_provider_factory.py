from app.cloud_provider.aws_provider import AwsProvider
from app.cloud_provider.cloud_provider import CloudProvider
from app.services.environement_varriables import get_env_variables
from urllib.parse import urlparse


class CloudProviderFactory:
    @staticmethod
    def get_cloud_provider(provider: str) -> CloudProvider:

        if provider == "s3":
            variables = get_env_variables(
                variables=[
                    "AWS_ACCESS_KEY",
                    "AWS_SECRET_KEY",
                    "AWS_REGION",
                    "AWS_BUCKET"
                ]
            )

            return AwsProvider(
                access_key=variables["AWS_ACCESS_KEY"],
                secret_key=variables["AWS_SECRET_KEY"],
                region=variables["AWS_REGION"],
                bucket=variables["AWS_BUCKET"],
            )
        else:
            raise ValueError(f"Provider {provider} not supported")
