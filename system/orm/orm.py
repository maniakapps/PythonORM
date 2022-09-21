"""Create, delete and update records with SQLAlchemy's ORM."""
#  __Author__= "Manuel Pizano"
#  __Email__= "doomclass@proton.me"
#  __Website__= "https://github.com/maniakapps"
#  __Portfolio__= "https://portafoliofullstack.vercel.app/"
#
#  Copyright (c) 2022.

#  __Author__=Manuel Pizano
#  __Email__=doomclass@proton.me
#  __Website__=https://github.com/maniakapps
#  __Portfolio__=https://portafoliofullstack.vercel.app/
#
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from logger import LOGGER
from system.relationships.models import Passenger


def orm_create_passenger(session: Session, passenger: Passenger) -> Passenger:
    """
    Create a new instance of our `User` model.

    :param passenger: a passenger object
    :param session: SQLAlchemy database session.
    :type session: Session

    :return: User
    """
    try:
        session.add(passenger)  # Add the user
        session.commit()  # Commit the change
        LOGGER.success(f"Created new passenger: {passenger}")
        return passenger
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when creating user: {e}")
        raise e


def orm_delete_passenger(session: Session, passenger: Passenger):
    """
    Delete a user if it exists.

    :param passenger: the passenger to remove
    :param session: SQLAlchemy database session.
    :type session: Session


    :return: None
    """
    try:
        session.delete(passenger)  # Delete the user
        session.commit()  # Commit the change
        LOGGER.success(f"Deleted passenger: {passenger}")
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when deleting user: {e}")
        raise e
