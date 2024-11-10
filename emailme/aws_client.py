from dataclasses import dataclass
from pathlib import Path

import boto3
import toml

AWS_CONFIG_PATH = Path("/etc/emailme/aws.toml")


@dataclass
class AWSConfig:
    sender: str
    aws_access_key: str
    aws_secret_key: str
    aws_region: str


def get_client():
    """
    Get an SES client using the AWS configuration.
    """
    check_aws_config()
    config = load_aws_config()
    return boto3.client(
        "ses",
        aws_access_key_id=config.aws_access_key,
        aws_secret_access_key=config.aws_secret_key,
        region_name=config.aws_region,
    )


def check_aws_config():
    if not AWS_CONFIG_PATH.exists():
        print(f"{AWS_CONFIG_PATH} does not exist.\nRun `sudo emailme aws` to create the file.")
        exit(1)


def load_aws_config():
    with open(AWS_CONFIG_PATH) as f:
        aws_config = toml.load(f)

    required_fields = list(AWSConfig.__dataclass_fields__.keys())
    for field in required_fields:
        if field not in aws_config:
            print(f"Missing required field: {field}")
            print("Run `sudo emailme aws` to create configuration file.")
            exit(1)

    return AWSConfig(**aws_config)
