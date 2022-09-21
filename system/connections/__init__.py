#  __Author__= "Manuel Pizano"
#  __Email__= "doomclass@proton.me"
#  __Website__= "https://github.com/maniakapps"
#  __Portfolio__= "https://portafoliofullstack.vercel.app/"
#
#  Copyright (c) 2022.
from database import engine
from .queries import *


def execute_queries():
    """
    Fetch and update records using raw SQL queries.

    :return: None
    """
    fetch_airports(engine)
    fetch_airlines(engine)
    fetch_passengers(engine)
    fetch_bookings(engine)
