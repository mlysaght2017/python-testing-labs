import unittest
from unittest.mock import patch, MagicMock
import botocore
import my_amazing_app


class TestMyAmazingApp(unittest.TestCase):
    @patch("my_amazing_app.boto3.client")
    def test_get_variable(self, mock_boto3_client):

        response = {"Parameter": {"Name": "MyTestParameterName", "Value": "myValue"}}

        # Reason for the next line is that by default mock creates a new mock object for all return values not explicitly set.
        # Without explicitly setting the return value, the object that get_parameter() is being called on would be different to the
        # one we are attempting to set a return value on.
        mock_boto3_client.return_value = mock_boto3_client
        mock_boto3_client.get_parameter.return_value = response

        result_value = my_amazing_app.get_variable("MyTestParameterName")

        mock_boto3_client.assert_called_with("ssm")
        mock_boto3_client().get_parameter.assert_called_with(Name="MyTestParameterName")

        self.assertEqual("myValue", result_value)

    @patch("my_amazing_app.boto3.resource")
    def test_store_data_unauthorized(self, boto3_resource):
        boto3_resource.return_value.Object.return_value.upload_file.side_effect = (
            botocore.exceptions.ClientError(
                {"Error": {"Code": "403", "Message": "Unauthorized"}}, "PutObject"
            )
        )
        return_value = my_amazing_app.store_data("test", "bucket", "key")
        boto3_resource.assert_called_with("s3")
        self.assertEqual("Fail", return_value)


if __name__ == "__main__":
    unittest.main()
