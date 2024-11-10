from pathlib import Path
from dataclasses import dataclass

import toml

EMAILME_CONFIG_PATH = Path.home() / ".config" / "emailme" / "config.toml"


@dataclass
class EmailMeConfig:
    recipient: str


def get_config():
    check_config()

    with open(EMAILME_CONFIG_PATH) as f:
        config = toml.load(f)

    return EmailMeConfig(**config)


def check_config():
    if not EMAILME_CONFIG_PATH.exists():
        print(f"{EMAILME_CONFIG_PATH} does not exist.\nRun `emailme configure` to create the file.")
        exit(1)
