"""Purge all data from database."""
#  __Author__= "Manuel Pizano"
#  __Email__= "doomclass@proton.me"
#  __Website__= "https://github.com/maniakapps"
#  __Portfolio__= "https://portafoliofullstack.vercel.app/"
#
#  Copyright (c) 2022.

from sqlalchemy import text
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from database import session
from logger import LOGGER
from system.relationships.models import Base


def cleanup_data():
    """ Removes all the tables' contents """
    try:
        session.execute(text("SET FOREIGN_KEY_CHECKS=0;"))
        session.commit()
        for table in reversed(Base.metadata.sorted_tables):
            # truncate table airport restart identity cascade;
            session.execute(text(f"TRUNCATE TABLE {table.name} restart identity cascade;"))
            session.commit()
        session.execute(text("SET FOREIGN_KEY_CHECKS=1;"))
        session.commit()
        LOGGER.success("Successfully reset all data.")
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when resetting data: {e}")
        raise e
