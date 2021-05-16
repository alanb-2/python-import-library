import logging
import sys

from argparse import ArgumentParser, Namespace
from config import Config
from yamlparser.yamlparser import YamlParser

LOGGER = logging.getLogger(__name__)


def get_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("--config-filepath", type=str, help="Filepath of configuration", required=True)
    parser.add_argument("--log-level", type=str, help="Logging level", default="INFO")

    return parser.parse_args()


def initialise_logging(log_level: str = "INFO") -> None:
    logging.basicConfig(
        stream=sys.stdout,
        format="%(asctime)s %(levelname)-8s %(message)s",
        level=log_level,
        datefmt="%Y-%m-%d %H:%M:%S"
    )


def main(config_filepath: str) -> None:

    yaml_parser = YamlParser(config_filepath, Config)
    config = yaml_parser.read()

    logging.info(f"application_name={config.application_name}")
    logging.info(f"memory={config.memory}")
    logging.info(f"workers={config.workers}")
    logging.info(f"log_level={config.log_level}")
    logging.info(f"dynamic_scaling={config.dynamic_scaling}")

    return None


if __name__ == "__main__":
    args = get_args()
    initialise_logging(args.log_level)
    main(args.config_filepath)
