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
import datetime

from database import session
from .orm import *


def create_and_delete_passengers():
    """
    Create a passenger record via SQLAlchemy's ORM, and subsequently delete it.

    :return: None
    """
    passenger = Passenger(
        first_name="TestFN",
        last_name="TestLN",
        date_of_birth=datetime.datetime.fromisocalendar(1997, 8, 20),
        country_of_citizenship="testCountry",
        country_of_residence="testResidency",
        passport_number="TEST1234",
        created_at=datetime.datetime.now(),
    )
    passenger = orm_create_passenger(session, passenger)
    orm_delete_passenger(session, passenger)
