import boto3
import os
import json
from moto import mock_s3
from lambda.fetch_facebook_ads.handler import lambda_handler

@mock_s3
def test_lambda_facebook_upload():
    os.environ['LANDING_BUCKET'] = 'test-bucket'
    os.environ['FB_ACCESS_TOKEN'] = 'dummy'
    os.environ['FB_AD_ACCOUNT_ID'] = 'act_123'
    
    s3 = boto3.client('s3', region_name='us-east-1')
    s3.create_bucket(Bucket='test-bucket')

    # Mocking the Facebook API would be required here; skipped for brevity.
    event = {}
    context = type('obj', (object,), {'aws_request_id' : 'test'})
    response = lambda_handler(event, context)
    assert response['statusCode'] == 200
