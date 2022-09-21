"""Perform JOIN queries on models with relationships."""
#  __Author__= "Manuel Pizano"
#  __Email__= "doomclass@proton.me"
#  __Website__= "https://github.com/maniakapps"
#  __Portfolio__= "https://portafoliofullstack.vercel.app/"
#
#  Copyright (c) 2022.

from sqlalchemy.orm import Session

from logger import LOGGER
from serializers.serialize import *
from system.relationships.models import Passenger, Flight, Booking, FlightManifest


def get_all_flights(session: Session, passenger: Passenger) -> None:
    """
    Fetch all flights belonging to a passenger.

    :param passenger: Used to consult the data
    :param session: SQLAlchemy database session.
    :type session: Session
    :return: None
    """
    flights = (
        session.query(Booking)
        .join(Flight, Flight.id == Booking.flight_id)
        .join(FlightManifest, Flight.id == FlightManifest.flight_id)
        .filter_by(passenger_id=passenger.id)
        .all()
    )
    for flight in flights:
        flight_record = serialize_flight(flight)
        LOGGER.info(flight_record)


def get_booking_info(session, booking: Booking, flight: Flight):
    info = (
        session.query(Booking)
        .join(Flight, flight.id == booking.flight_id)
        .filter_by(id=booking.id)
        .first()
    )
    booking_info = serialize_booking(info)
    LOGGER.info(booking_info)
