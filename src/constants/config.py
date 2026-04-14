import yaml


def load_config(path="src\constants\config.yaml"):
    with open(path, "r") as f:
        config = yaml.safe_load(f)
    return config

config = load_config()