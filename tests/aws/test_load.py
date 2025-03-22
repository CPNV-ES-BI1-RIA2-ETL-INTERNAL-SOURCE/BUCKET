import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import json
from unittest.mock import patch, Mock
from botocore.exceptions import ClientError
from fastapi.testclient import TestClient

from app.exceptions.environement_variables_exception import EnvironmentVariableException
from app.main import app
import io

class TestLoad:
    _PDF_FILE_PATH = "./tests/sample.pdf"

    def client_init(self):
        try:
            return TestClient(app)
        except EnvironmentVariableException as e:
            print("Error:", e)

    @patch("app.cloud_provider.aws_provider.AwsProvider.connect", Mock(return_value=None))
    @patch("app.cloud_provider.aws_provider.AwsProvider.load", Mock(return_value="http://mock-data-source.com"))
    def test_load_pdf_success(self):
        # Given
        client = self.client_init()
        with open(self._PDF_FILE_PATH, "rb") as file:
            file_data = io.BytesIO(file.read())
            payload = {
                "file": ("sample.pdf", file_data, "application/pdf"),
            }

            # When
            response = client.post(
                "/api/v2/objects?destination=uploads/documents",
                files=payload
            )

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
        with open(self._PDF_FILE_PATH, "rb") as file:
            file_data = io.BytesIO(file.read())
            payload = {
                "file": ("sample.pdf", file_data, "application/pdf"),
            }

            # When
            response = client.post(
                "/api/v2/objects?destination=uploads/documents",
                files=payload
            )

            # Then
            assert response.status_code == 500