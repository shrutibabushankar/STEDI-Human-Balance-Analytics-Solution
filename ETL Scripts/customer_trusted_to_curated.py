import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://shruti-lake-house/accelerometer_landing/"],
        "recurse": True,
    },
    transformation_ctx="S3bucket_node1",
)

# Script generated for node Amazon S3
AmazonS3_node1692188195461 = glueContext.create_dynamic_frame.from_options(
    format_options={},
    connection_type="s3",
    format="parquet",
    connection_options={
        "paths": ["s3://shruti-lake-house/customer_trusted/"],
        "recurse": True,
    },
    transformation_ctx="AmazonS3_node1692188195461",
)

# Script generated for node Join
Join_node1692188245686 = Join.apply(
    frame1=S3bucket_node1,
    frame2=AmazonS3_node1692188195461,
    keys1=["user"],
    keys2=["email"],
    transformation_ctx="Join_node1692188245686",
)

# Script generated for node Drop Fields
DropFields_node1692188265804 = DropFields.apply(
    frame=Join_node1692188245686,
    paths=["timeStamp", "user", "x", "y", "z"],
    transformation_ctx="DropFields_node1692188265804",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1692188265804,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://shruti-lake-house/customers_curated/",
        "partitionKeys": [],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="S3bucket_node3",
)

job.commit()
