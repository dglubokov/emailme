import toml

from emailme.config import EmailMeConfig, EMAILME_CONFIG_PATH


def run(args):
    # Make directory if it doesn't exist
    EMAILME_CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)

    keys = EmailMeConfig.__dataclass_fields__.keys()

    values = {}
    for key in keys:
        value = input(f"Enter {key}: ")
        values[key] = value

    with open(EMAILME_CONFIG_PATH, "w") as f:
        toml.dump(values, f)

    print(f"Configuration saved to {EMAILME_CONFIG_PATH}")
