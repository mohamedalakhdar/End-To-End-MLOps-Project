import yaml

DEFAULT_CONFIG_PATH = "configs/config.yaml"


def load_config(path=DEFAULT_CONFIG_PATH):
    """Load and parse the YAML pipeline config into a dict."""

    with open(path) as f:
        return yaml.safe_load(f)
