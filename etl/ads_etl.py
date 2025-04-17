#!/usr/bin/env python3
import sys
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(
    sys.argv,
    ['JOB_NAME','BUCKET','REDSHIFT_URL','REDSHIFT_TEMP_DIR','REDSHIFT_DBTABLE','REDSHIFT_USER','REDSHIFT_PASSWORD']
)
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Read JSONs from S3
datasource = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [f"s3://{args['BUCKET']}/facebook"], "recurse": True},
    format="json"
)

df = datasource.toDF()
df = df.selectExpr(
    "campaign_name", "impressions", "clicks", "spend",
    "cast(date_start as date) as date"
)

# Write to Redshift
df.write   .format("com.databricks.spark.redshift")   .option("url", args["REDSHIFT_URL"])   .option("dbtable", args["REDSHIFT_DBTABLE"])   .option("user", args["REDSHIFT_USER"])   .option("password", args["REDSHIFT_PASSWORD"])   .option("tempdir", args["REDSHIFT_TEMP_DIR"])   .mode("append")   .save()
