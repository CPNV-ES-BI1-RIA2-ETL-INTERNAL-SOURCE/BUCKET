from app.cloud_provider.aws_provider import AwsProvider
from app.cloud_provider.cloud_provider import CloudProvider
from app.services.environement_varriables import get_env_variables
from urllib.parse import urlparse

class CloudProviderFactory:
    @staticmethod
    def get_cloud_provider(url: str) -> CloudProvider:

        variables = get_env_variables(variables=["AWS_ACCESS_KEY", "AWS_SECRET_KEY", "AWS_REGION"])

        parsed_url = urlparse(url)
        provider = parsed_url.scheme
        bucket = parsed_url.netloc
        path = parsed_url.path.lstrip('/')

        if provider == "s3" :
            return  AwsProvider(
                access_key=variables["AWS_ACCESS_KEY"],
                secret_key=variables["AWS_SECRET_KEY"],
                region=variables["AWS_REGION"],
                bucket=bucket,
                destination=path
            )
        else:
            raise ValueError(f"Invalid cloud provider for path: {path}")