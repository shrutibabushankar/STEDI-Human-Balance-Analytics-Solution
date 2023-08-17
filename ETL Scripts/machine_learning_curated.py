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

# Script generated for node Acce Trusted Bucket
AcceTrustedBucket_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={},
    connection_type="s3",
    format="parquet",
    connection_options={"paths": ["s3://shruti-lake-house/accelerometer_trusted/"]},
    transformation_ctx="AcceTrustedBucket_node1",
)

# Script generated for node Step Trainer Trusted
StepTrainerTrusted_node1692188195461 = glueContext.create_dynamic_frame.from_options(
    format_options={},
    connection_type="s3",
    format="parquet",
    connection_options={"paths": ["s3://shruti-lake-house/step_trainer_trusted/"]},
    transformation_ctx="StepTrainerTrusted_node1692188195461",
)

# Script generated for node Join
Join_node1692188245686 = Join.apply(
    frame1=AcceTrustedBucket_node1,
    frame2=StepTrainerTrusted_node1692188195461,
    keys1=["timeStamp"],
    keys2=["sensorReadingTime"],
    transformation_ctx="Join_node1692188245686",
)

# Script generated for node Machine Learning Curated
MachineLearningCurated_node3 = glueContext.write_dynamic_frame.from_options(
    frame=Join_node1692188245686,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://shruti-lake-house/machine_learning_curated/",
        "partitionKeys": [],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="MachineLearningCurated_node3",
)

job.commit()
