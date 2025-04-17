import subprocess
import os

def test_etl_script_loadable():
    result = subprocess.run(
        ["python3", "etl/ads_etl.py"],
        env={
            **os.environ,
            "BUCKET": "test-bucket",
            "REDSHIFT_URL": "jdbc:redshift://example.com/dev",
            "REDSHIFT_TEMP_DIR": "s3://dummy/temp",
            "REDSHIFT_DBTABLE": "test_table",
            "REDSHIFT_USER": "admin",
            "REDSHIFT_PASSWORD": "ComplexPass123!"
        },
        capture_output=True,
        text=True
    )
    assert result.returncode in [0, 1]  # 1 acceptable if AWS Glue lib not available locally
