"""Run source code for each tutorial found on HackersAndSlackers."""
#  __Author__= "Manuel Pizano"
#  __Email__= "doomclass@proton.me"
#  __Website__= "https://github.com/maniakapps"
#  __Portfolio__= "https://portafoliofullstack.vercel.app/"
#
#  Copyright (c) 2022.

from config import CLEANUP_DATA
from logger import LOGGER
from system.clean import cleanup_data
from system.connections import execute_queries
from system.orm import create_and_delete_passengers
from system.relationships import create_relationships


def init_script():
    """Run all scripts."""

    # Part 1: Executing SELECT and UPDATE queries with an SQLAlchemy engine
    LOGGER.info("----------------------------------------------------")
    LOGGER.info("Part 1: Executing queries against an SQLAlchemy engine.")
    execute_queries()

    # Part 2: Implementing an ORM
    LOGGER.info("----------------------------------------------------")
    LOGGER.info("Part 2: Create and delete records from a data model.")
    create_and_delete_passengers()

    # Part 3: ORM relationships
    LOGGER.info("----------------------------------------------------")
    LOGGER.info("Part 3: Utilize relationships to execute JOINs.")
    create_relationships()

    # OPTIONAL: Reset table data after each run
    if CLEANUP_DATA:
        LOGGER.info("----------------------------------------------------")
        LOGGER.info("Purging all created data...")
        cleanup_data()
