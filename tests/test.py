#  __Author__= "Manuel Pizano"
#  __Email__= "doomclass@proton.me"
#  __Website__= "https://github.com/maniakapps"
#  __Portfolio__= "https://portafoliofullstack.vercel.app/"
#
#  Copyright (c) 2022.

import unittest
from datetime import datetime

from database.connect import session, engine
from system.relationships.models import Airline, Base


class TestApp(unittest.TestCase):

    def setUp(self):
        self.session = session
        self.engine = engine
        Base.metadata.create_all(self.engine)
        self.airline = Airline(
            airline_code="IBM",
            airline_name="Inbursa MX",
            airline_country="Mexico",
            created_at=datetime.now()
        )
        self.session.add(self.airline)
        self.session.commit()

    def tearDown(self) -> None:
        Base.metadata.drop_all(self.engine)

    def test_create_airline_object_exists(self):
        result = self.session.query(Airline).first()
        self.assertEqual(self.airline, result)
