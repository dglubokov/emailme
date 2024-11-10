import toml

from emailme.aws_client import AWSConfig, AWS_CONFIG_PATH


def run(args):
    # Make directory if it doesn't exist
    AWS_CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)

    keys = AWSConfig.__dataclass_fields__.keys()

    values = {}
    for key in keys:
        value = input(f"Enter {key}: ")
        values[key] = value

    with open(AWS_CONFIG_PATH, "w") as f:
        toml.dump(values, f)

    print(f"Configuration saved to {AWS_CONFIG_PATH}")
