import json
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
            "uri": "s3://mock-bucket-name",
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
            "uri": "s3://mock-bucket-name",
            "recurse": False
        }

        # When
        response = client.get("/api/v2/objects", params=params)

        # Then
        assert response.status_code == 500
        assert "Access Denied" in response.json()["detail"]