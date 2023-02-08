"""Custom logger."""
#  __Author__= "Manuel Pizano"
#  __Email__= "doomclass@proton.me"
#  __Website__= "https://github.com/maniakapps"
#  __Portfolio__= "https://portafoliofullstack.vercel.app/"
#
#  Copyright (c) 2022.

import logging
from rich.logging import RichHandler


def formatter(record):
    if record.levelname == "WARNING":
        return f"[light-yellow]{record.levelname}:[/light-yellow] [light-white]{record.msg}[/light-white]"
    elif record.levelname == "ERROR":
        return f"[light-red]{record.levelname}:[/light-red] [light-white]{record.msg}[/light-white]"
    elif record.levelname == "SUCCESS":
        return f"[light-green]{record.levelname}:[/light-green] [light-white]{record.msg}[/light-white]"
    else:
        return f"[#67c9c4]{record.levelname}:[/#67c9c4] [light-white]{record.msg}[/light-white]"


def create_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    handler = RichHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


LOGGER = create_logger(__name__)
