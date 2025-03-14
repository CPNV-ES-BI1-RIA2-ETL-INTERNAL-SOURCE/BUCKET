from botocore.exceptions import ClientError
from app.cloud_provider.cloud_provider import CloudProvider
from app.exceptions.authentication_failed_exception import AuthenticationFailedException
from app.exceptions.destination_not_found_exception import DestinationNotFoundException
from app.exceptions.object_alread_exist_exception import ObjectAlreadyExistException
import boto3
from typing import List


class AwsProvider(CloudProvider):
    """
    Service to interact with AWS S3.
    """
    def __init__(self, access_key: str, secret_key: str, bucket: str, region: str, destination: str) -> None:
        self._access_key = access_key
        self._secret_key = secret_key
        self._bucket = bucket
        self._region_name = region
        self._destination_name = destination
        self._connection = None  # Initialize the connection to None

    def connect(self) -> None:
        """
        Connect to the AWS S3 service.
        """
        try:
            self._connection = boto3.client(
                's3',
                aws_access_key_id=self._access_key,
                aws_secret_access_key=self._secret_key,
                region_name=self._region_name
            )
        except ClientError as e:
            raise AuthenticationFailedException(f"Authentication failed: {e.response['Error']['Message']}")
        except Exception as e:
            raise AuthenticationFailedException("Authentication has failed!")

    def disconnect(self) -> None:
        """
        Disconnect from the AWS S3 service.
        Note: boto3 does not explicitly require a disconnection.
        """
        self._connection.close()
        self._connection = None  # Optional, but explicit

    def load(self, data: str) -> str:
        """
        Upload a binary object to the specified bucket.

        :param data: data to upload.
        :raises DestinationNotFoundException: If the bucket does not exist.
        :raises ObjectAlreadyExistException: If a precondition conflict occurs.
        """
        if not self._connection:
            raise RuntimeError("AWS service is not connected. Call connect() first.")

        try:
            self._connection.put_object(
                Bucket=self._bucket,
                Key=self._destination_name,
                Body=data
            )

            url = self._connection.generate_presigned_url(
                ClientMethod='get_object',
                Params={
                    'Bucket': self._bucket,
                    'Key': self._destination_name
                },
                ExpiresIn=604800
            )

            return url

        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'NoSuchBucket':
                raise DestinationNotFoundException("Destination not found!")
            if error_code == 'PreconditionFailed':
                raise ObjectAlreadyExistException("Object already exists!")
            raise

    def list(self, recurse: bool) -> List[str]:
        """
        List the objects in the specified bucket.

        :param recurse: whether to list recursively.
        :return: a list of object keys.
        :raises DestinationNotFoundException: If the bucket does not exist.
        """
        if not self._connection:
            raise RuntimeError("AWS service is not connected. Call connect() first.")

        try:
            response = self._connection.list_objects_v2(
                Bucket=self._bucket
            )

            if 'Contents' not in response:
                return []

            keys = [obj['Key'] for obj in response['Contents']]
            return keys

        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'NoSuchBucket':
                raise DestinationNotFoundException("Destination not found!")
            raise
