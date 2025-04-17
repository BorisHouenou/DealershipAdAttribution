import boto3
import os
import json
from moto import mock_s3
from lambda.webhook_listener.handler import lambda_handler

@mock_s3
def test_webhook_listener():
    os.environ['LANDING_BUCKET'] = 'test-bucket'
    s3 = boto3.client('s3', region_name='us-east-1')
    s3.create_bucket(Bucket='test-bucket')

    event = {"body": json.dumps({"customer_id": 1, "event": "test_drive"})}
    context = type('obj', (object,), {'aws_request_id': '123abc'})
    response = lambda_handler(event, context)
    assert response['statusCode'] == 200
