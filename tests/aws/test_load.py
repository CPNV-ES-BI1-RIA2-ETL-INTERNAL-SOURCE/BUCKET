import json
from unittest.mock import patch, Mock
from botocore.exceptions import ClientError
from fastapi.testclient import TestClient

from app.exceptions.environement_varriables_exception import EnvironmentVariableException
from app.main import app


class TestLoad:
    _JSON_FILE_PATH = "../stationboard-Lausanne-01.12.2024-00.01-ALL.json"

    def client_init(self):
        try:
            return TestClient(app)
        except EnvironmentVariableException as e:
            print("Error:", e)

    @patch("app.cloud_provider.aws_provider.AwsProvider.connect", Mock(return_value=None))
    @patch("app.cloud_provider.aws_provider.AwsProvider.load", Mock(return_value="http://mock-data-source.com"))
    def test_load_json_success(self):
        # Given
        client = self.client_init()
        with open(self._JSON_FILE_PATH, "r") as file:
            json_file = json.load(file)
            payload = {
                "data": json.dumps(json_file, indent=4),
                "dataDestination": "s3://mock-destination-bucket/file.csv",
            }

            # When
            response = client.post("/job", json=payload)

            # Then
            assert response.status_code == 200

    @patch("app.cloud_provider.aws_provider.AwsProvider.connect", Mock(side_effect=ClientError({
        'Error': {
            'Code': 'PreconditionFailed',
            'Message': 'Object already exists!'
        }
    }, "PutObject")))
    @patch("app.cloud_provider.aws_provider.AwsProvider.load", Mock(return_value="http://mock-data-source.com"))
    def test_document_already_exists(self):
        # Given
        client = self.client_init()
        with open(self._JSON_FILE_PATH, "rb") as file:
            json_file = json.load(file)

            payload = {
                "data": json.dumps(json_file, indent=4),
                "dataDestination": "s3://mock-destination-bucket/file.csv",
            }

            # When
            response = client.post("/job", json=payload)

            # Then
            assert response.status_code == 500
