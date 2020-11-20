import unittest
from unittest.mock import patch
import botocore

import my_amazing_app

class TestMyAmazingApp(unittest.TestCase):
    
    @patch('my_amazing_app.boto3.client')
    def test_get_variable(self, mock_boto3_client):
        
        response = {
            'Parameter': {
                'Name': 'MyTestParameterName',
                'Value': 'myValue'
            }
        }
        
        mock_boto3_client.return_value = mock_boto3_client
        mock_boto3_client.get_parameter.return_value = response
        
        result_value = my_amazing_app.get_variable("MyTestParameterName")
        
        self.assertEqual("myValue", result_value)
        mock_boto3_client.assert_called_with("ssm")
        mock_boto3_client().get_parameter.assert_called_with(Name="MyTestParameterName")
        
    @patch('my_amazing_app.boto3.resource')    
    def test_store_data(self, boto3_resource):
        my_amazing_app.store_data("test", "bucket", "key")
        boto3_resource.assert_called_with("s3")

    @patch('my_amazing_app.boto3.resource')    
    def test_store_data_unauthorized(self, boto3_resource):
        boto3_resource.return_value.Object.return_value.upload_file.side_effect = botocore.exceptions.ClientError(
            {"Error": {"Code": "403", "Message": "Unauthorized"}}, "PutObject"    
        )
        return_value = my_amazing_app.store_data("test", "bucket", "key")
        boto3_resource.assert_called_with("s3")
        self.assertEqual("we have a problem", return_value)
        
if __name__ == '__main__':
    unittest.main()