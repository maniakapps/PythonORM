"""Execute raw SQL queries against an SQLAlchemy engine."""
#  __Author__= "Manuel Pizano"
#  __Email__= "doomclass@proton.me"
#  __Website__= "https://github.com/maniakapps"
#  __Portfolio__= "https://portafoliofullstack.vercel.app/"
#
#  Copyright (c) 2022.
from typing import List, Optional

from sqlalchemy import text
from sqlalchemy.engine.base import Engine

from logger import LOGGER


def fetch_airports(engine: Engine) -> Optional[List[dict]]:
    """
    Select rows from database and parse as list of dicts.

    :param engine: Database engine to handle raw SQL queries.
    :type engine: engine

    :return: Optional[List[dict]]
    """
    result = engine.execute(
        text(
            "SELECT id, airport_name, country, state, \
            city, created_at, updated_at \
            FROM airport ORDER BY id LIMIT 10;"
        )
    )
    rows = [dict(row) for row in result.fetchall()]
    LOGGER.info(f"Selected {result.rowcount} rows: {rows}")
    return rows


def fetch_airlines(engine: Engine) -> Optional[List[dict]]:
    """
    Select rows from database and parse as list of dicts.

    :param engine: Database engine to handle raw SQL queries.
    :type engine: engine

    :return: Optional[List[dict]]
    """
    result = engine.execute(
        text(
            "SELECT * \
            FROM airline ORDER BY id LIMIT 10;"
        )
    )
    rows = [dict(row) for row in result.fetchall()]
    LOGGER.info(f"Selected {result.rowcount} rows: {rows}")
    return rows


def fetch_passengers(engine: Engine) -> Optional[List[dict]]:
    """
    Select rows from database and parse as list of dicts.

    :param engine: Database engine to handle raw SQL queries.
    :type engine: engine

    :return: Optional[List[dict]]
    """
    result = engine.execute(
        text(
            "SELECT * \
            FROM passenger ORDER BY id LIMIT 10;"
        )
    )
    rows = [dict(row) for row in result.fetchall()]
    LOGGER.info(f"Selected {result.rowcount} rows: {rows}")
    return rows


def fetch_bookings(engine: Engine) -> Optional[List[dict]]:
    """
    Select rows from database and parse as list of dicts.

    :param engine: Database engine to handle raw SQL queries.
    :type engine: engine

    :return: Optional[List[dict]]
    """
    result = engine.execute(
        text(
            "SELECT * \
            FROM booking ORDER BY id LIMIT 10;"
        )
    )
    rows = [dict(row) for row in result.fetchall()]
    LOGGER.info(f"Selected {result.rowcount} rows: {rows}")
    return rows
