import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from unittest.mock import patch, Mock
from botocore.exceptions import ClientError
from fastapi.testclient import TestClient

from app.exceptions.environement_varriables_exception import EnvironmentVariableException
from app.main import app


class TestList:
    def client_init(self):
        try:
            return TestClient(app)
        except EnvironmentVariableException as e:
            print("Error:", e)

    @patch("app.cloud_provider.aws_provider.AwsProvider.connect", Mock(return_value=None))
    @patch("app.cloud_provider.aws_provider.AwsProvider.list", Mock(return_value=["file1.txt", "file2.txt"]))
    def test_list_objects_success(self):
        # Given
        client = self.client_init()
        params = {
            "recurse": False
        }

        # When
        response = client.get("/api/v2/objects", params=params)

        # Then
        assert response.status_code == 200
        assert response.json() == {"objects": ["file1.txt", "file2.txt"]}

    @patch("app.cloud_provider.aws_provider.AwsProvider.connect", Mock(side_effect=ClientError({
        'Error': {
            'Code': 'AccessDenied',
            'Message': 'Access Denied'
        }
    }, "ListObjectsV2")))
    def test_list_objects_access_denied(self):
        # Given
        client = self.client_init()
        params = {
            "recurse": False
        }

        # When
        response = client.get("/api/v2/objects", params=params)

        # Then
        assert response.status_code == 500
        assert "Access Denied" in response.json()["detail"]

    @patch("boto3.client")
    def test_list_objects_success_with_recurse(self, mock_boto_client):
        # Mock the boto3 S3 client
        mock_s3_client = Mock()
        mock_boto_client.return_value = mock_s3_client

        # Mock the response from list_objects_v2
        mock_s3_client.list_objects_v2.return_value = {
            "Contents": [
                {"Key": "folder/folder2/folder3/file.csv"},
                {"Key": "folder/file1.txt"},
                {"Key": "file2.txt"}
            ]
        }

        # Given
        client = self.client_init()
        params = {
            "recurse": True
        }

        # When
        response = client.get("/api/v2/objects", params=params)

        # Then
        assert response.status_code == 200
        assert response.json() == {
            "objects": [
                "folder/folder2/folder3/file.csv",
                "folder/file1.txt",
                "file2.txt"
            ]
        }
