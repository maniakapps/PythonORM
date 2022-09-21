#  __Author__= "Manuel Pizano"
#  __Email__= "doomclass@proton.me"
#  __Website__= "https://github.com/maniakapps"
#  __Portfolio__= "https://portafoliofullstack.vercel.app/"
#
#  Copyright (c) 2022.

from database import session
from system.relationships.joins import get_all_flights, get_booking_info
from system.relationships.objects import create_airlines_object, create_booking_object, create_passenger_object, \
    create_flight_object, create_airport_object
from system.relationships.orm import create_airline, create_booking, create_passenger


def create_relationships():
    """
    Use SQLAlchemy's ORM to create objects with relationships.
    :return: None
    """

    # create airports
    airport1, airport2 = create_airport_object()

    # create passengers
    passenger_1, passenger_2 = create_passenger_object()
    passenger_1 = create_passenger(session, passenger_1)
    passenger_2 = create_passenger(session, passenger_2)

    # Create airlines
    airline_one, airline_two = create_airlines_object()
    airline_one = create_airline(session, airline_one)

    # create flights
    flight1, flight2 = create_flight_object(airline_one, airport1, airport2)

    # Create bookings
    booking_1, booking_2 = create_booking_object(passenger_1, flight1)
    booking_1 = create_booking(session, booking_1)
    booking_2 = create_booking(session, booking_2)

    # Display booking info
    get_booking_info(session, booking_1, passenger_1)
    get_booking_info(session, booking_2, passenger_1)

    # One-to-many JOIN for a given user
    get_all_flights(session, passenger_1)
    get_all_flights(session, passenger_2)
