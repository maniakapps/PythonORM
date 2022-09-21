#  __Author__= "Manuel Pizano"
#  __Email__= "doomclass@proton.me"
#  __Website__= "https://github.com/maniakapps"
#  __Portfolio__= "https://portafoliofullstack.vercel.app/"
#
#  Copyright (c) 2022.

from datetime import datetime
from typing import Tuple

from system.relationships.models import Airline, Airport, Passenger, Booking, Flight


def create_airlines_object() -> Tuple[Airline, Airline]:
    ibm = Airline(
        airline_code="IBM",
        airline_name="Inbursa MX",
        airline_country="Mexico",
        created_at=datetime.now()
    )
    air_canada = Airline(
        airline_code="ACA",
        airline_name="Air canada",
        airline_country="Canada",
        created_at=datetime.now()
    )
    return ibm, air_canada


def create_airport_object() -> Tuple[Airport, Airport]:
    aicm = Airport(
        airport_name="AICM",
        country="Mexico",
        state="CMDX",
        city="CDMX",
        created_at=datetime.now()
    )
    aifa = Airport(
        airport_name="AIFA",
        country="Mexico",
        state="CMDX",
        city="CDMX",
        created_at=datetime.now()
    )
    return aicm, aifa


def create_passenger_object():
    test = Passenger(
        first_name="A",
        last_name="B",
        date_of_birth=datetime.fromisocalendar(1997, 20, 8)
    )
    test2 = Passenger(
        first_name="X",
        last_name="Y",
        date_of_birth=datetime.fromisocalendar(1997, 20, 8)
    )
    return test, test2


def create_flight_object(airline: Airline, departing_airport: Airport, arriving_airport: Airport):
    """Creates a figlht object"""
    flight1 = Flight(
        departing_gate="first",
        arriving_gate="second",
        created_at=datetime.now(),
        airline_id=airline.id,
        departing_airport_id=departing_airport.id,
        arriving_airport_id=arriving_airport.id
    )
    flight2 = Flight(
        departing_gate="first",
        arriving_gate="second",
        created_at=datetime.now(),
        airline_id=airline.id,
        departing_airport_id=arriving_airport.id,
        arriving_airport_id=departing_airport.id
    )
    return flight1, flight2


def create_booking_object(passenger: Passenger, flight_id: Flight):
    booking1 = Booking(
        flight_id=flight_id.id,
        status="flying",
        booking_platform="Kayak",
        created_at=datetime.now(),
        passenger_id=passenger.id
    )
    booking2 = Booking(
        flight_id=flight_id.id,
        status="flying",
        booking_platform="Kayak",
        created_at=datetime.now(),
        passenger_id=passenger.id
    )
    return booking1, booking2
