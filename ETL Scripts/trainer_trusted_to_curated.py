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

# Script generated for node Step Trainer landing
StepTrainerlanding_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://shruti-lake-house/step_trainer_landing/"],
        "recurse": True,
    },
    transformation_ctx="StepTrainerlanding_node1",
)

# Script generated for node Customer Curated
CustomerCurated_node1692188195461 = glueContext.create_dynamic_frame.from_options(
    format_options={},
    connection_type="s3",
    format="parquet",
    connection_options={
        "paths": ["s3://shruti-lake-house/customers_curated/"],
        "recurse": True,
    },
    transformation_ctx="CustomerCurated_node1692188195461",
)

# Script generated for node Join
Join_node1692188245686 = Join.apply(
    frame1=StepTrainerlanding_node1,
    frame2=CustomerCurated_node1692188195461,
    keys1=["serialNumber"],
    keys2=["serialNumber"],
    transformation_ctx="Join_node1692188245686",
)

# Script generated for node Drop Fields
DropFields_node1692188265804 = DropFields.apply(
    frame=Join_node1692188245686,
    paths=[
        "`.serialNumber`",
        "birthDay",
        "shareWithPublicAsOfDate",
        "shareWithResearchAsOfDate",
        "registrationDate",
        "customerName",
        "shareWithFriendsAsOfDate",
        "email",
        "phone",
        "lastUpdateDate",
    ],
    transformation_ctx="DropFields_node1692188265804",
)

# Script generated for node Step Trainer Trusted
StepTrainerTrusted_node3 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1692188265804,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://shruti-lake-house/step_trainer_trusted/",
        "partitionKeys": [],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="StepTrainerTrusted_node3",
)

job.commit()
