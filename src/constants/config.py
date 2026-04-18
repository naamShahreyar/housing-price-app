import yaml
import os

def load_config():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(base_dir, "constants", "config.yaml")

    with open(path, "r") as f:
        return yaml.safe_load(f)

config = load_config()