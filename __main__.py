"""An AWS Python Pulumi program"""
import pulumi
from pulumi_aws import s3

# Create an S3 bucket
bucket = s3.Bucket(
    "my-sre-bucket",
    acl="private",  # Access control for the bucket
    tags={
        "Environment": "Dev",
        "Team": "SRE",
    },
)

# Export the bucket name
pulumi.export("bucket_name", bucket.id)

