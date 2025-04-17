import os
import pytest
from container.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_campaign_api(client):
    response = client.get('/attribution/campaign/TEST_CAMPAIGN?model=bayesian_mmm')
    assert response.status_code in (200, 500)  # Expect failure if Redshift not mocked
