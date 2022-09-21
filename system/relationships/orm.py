#  __Author__= "Manuel Pizano"
#  __Email__= "doomclass@proton.me"
#  __Website__= "https://github.com/maniakapps"
#  __Portfolio__= "https://portafoliofullstack.vercel.app/"
#
#  Copyright (c) 2022.

from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from logger import LOGGER
from system.relationships.models import Airline, Airport, Booking, Passenger


def create_airline(session: Session, airline: Airline):
    """Creates an airline using the ORM"""
    try:
        existing_airline = (
            session.query(Airline).filter(
                Airline.airline_name == airline.airline_name and airline.airline_code == Airline.airline_code).first()
        )
        if existing_airline is None:
            session.add(airline)
            session.commit()
            LOGGER.success(f"Created airline {airline}")
        else:
            LOGGER.warning(f"Airline already exists in database: {existing_airline}")
        return session.query(Airline).filter(
            Airline.airline_name == airline.airline_name and airline.airline_code == Airline.airline_code).first()
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when creating airline: {e}")
        raise e


def create_airport(session: Session, airport: Airport):
    try:
        existing_airport = (
            session.query(Airport).filter(
                Airport.airport_name == airport.airport_name).first()
        )
        if existing_airport is None:
            session.add(airport)
            session.commit()
            LOGGER.success(f"Created airport {airport}")
        else:
            LOGGER.warning(f"Airport already exists in database: {existing_airport}")
        return session.query(Airport).filter(Airport.airport_name == airport.airport_name).first()
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when creating airport: {e}")
        raise e


def create_booking(session: Session, booking: Booking):
    try:
        existing_booking = (
            session.query(Booking).filter(
                Booking.id == booking.id).first()
        )
        if existing_booking is None:
            session.add(booking)
            session.commit()
            LOGGER.success(f"Created booking {booking}")
        else:
            LOGGER.warning(f"Booking already exists in database: {existing_booking}")
        return session.query(Booking).filter(Booking.id == booking.id).first()
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when creating airport: {e}")
        raise e


def create_passenger(session: Session, passenger: Passenger):
    try:
        existing_passenger = (
            session.query(Passenger).filter(
                Passenger.id == passenger.id).first()
        )
        if existing_passenger is None:
            session.add(passenger)
            session.commit()
            LOGGER.success(f"Created passenger {passenger}")
        else:
            LOGGER.warning(f"Passenger already exists in database: {existing_passenger}")
        return session.query(Passenger).filter(Passenger.id == passenger.id).first()
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when creating airport: {e}")
        raise e
