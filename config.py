from __future__ import annotations
from typing import Final

import os
from dotenv import load_dotenv
from typing import Final

from logging.config import dictConfig

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

LOGGING_CONFIG = {
  "version": 1,
  "disabled_existing_loggers": False,
  "formatters": {
    "verbose": {
      "format": "%(levelname)-10s - %(asctime)s - %(module)-15s : %(message)s"
    },
    "standard": {
      "format": "%(levelname)-10s - %(name)-15s : %(message)s"
    },
  },
  "handlers": {
    "console": {
      "level": "DEBUG",
      "class": "logging.StreamHandler",
      "formatter": "standard",
    },
    "console2": {
      "level": "WARNING",
      "class": "logging.StreamHandler",
      "formatter": "standard",
    },
    "file": {
      "level": "INFO",
      "class": "logging.FileHandler",
      "filename": "logs/infos.log",
      "mode": "w",
      "formatter": "verbose",
    },
  },
  "loggers": {
    "bot": {
      "handlers": ["console"], 
      "level": "INFO", 
      "propagate": False
    },
    "discord": {
      "handlers": ["console2", "file"],
      "level": "INFO",
      "propagate": False,
    },
  },
}

dictConfig(LOGGING_CONFIG)