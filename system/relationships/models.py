#  __Author__= "Manuel Pizano"
#  __Email__= "doomclass@proton.me"
#  __Website__= "https://github.com/maniakapps"
#  __Portfolio__= "https://portafoliofullstack.vercel.app/"
#
#  Copyright (c) 2022.

from sqlalchemy import Column, String, DateTime, BigInteger, Text, Date, DECIMAL, func, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, backref

from database import engine

Base = declarative_base()


class Airport(Base):
    """Airport class
    """
    __tablename__ = "airport"
    id = Column(BigInteger, primary_key=True, autoincrement="auto")
    airport_name = Column(String(50), nullable=False, unique=True)
    country = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now(), nullable=True)

    def __eq__(self, other):
        return self.id == other.id and self.airport_name == other.airport_name

    def __repr__(self) -> str:
        return "<Airport %r>" % self.airport_name

    def __hash__(self):
        return hash(self)


class Flight(Base):
    """Flight class"""
    __tablename__ = "flight"
    id = Column(BigInteger, primary_key=True, autoincrement="auto")
    departing_gate = Column(String(20), nullable=False)
    arriving_gate = Column(String(20), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now(), nullable=True)  # relationship("Child", backref="parent")
    airline_id = Column(BigInteger, ForeignKey('airline.id'), nullable=False)
    airline = relationship(
        "Airline",
        backref=backref("flight_airline", cascade="all, delete-orphan"),
        foreign_keys=[airline_id]
    )
    departing_airport_id = Column(BigInteger, ForeignKey('airport.id'), nullable=False)
    departing_airport = relationship(
        "Airport",
        backref=backref("flight_departing", cascade="all, delete-orphan"),
        foreign_keys=[departing_airport_id]
    )
    arriving_airport_id = Column(BigInteger, ForeignKey('airport.id'), nullable=False)
    arriving_airport = relationship(
        "Airport",
        backref=backref("flight_arriving", cascade="all, delete-orphan"),
        foreign_keys=[arriving_airport_id]
    )

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self) -> str:
        return "<Flight %r>" % self.id

    def __hash__(self):
        return hash(self)


class Airline(Base):
    __tablename__ = "airline"
    id = Column(BigInteger, primary_key=True, autoincrement="auto")
    airline_code = Column(String, nullable=False, unique=True)
    airline_name = Column(String, nullable=False)
    airline_country = Column(String(50), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now(), nullable=True)

    def __repr__(self) -> str:
        return "<Airline %r>" % self.airline_name

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self)


class BoardingPass(Base):
    __tablename__ = "boarding_pass"
    id = Column(BigInteger, primary_key=True, autoincrement="auto")
    qr_code = Column(Text, unique=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())
    booking_id = Column(BigInteger, ForeignKey('booking.id'), nullable=False)
    booking = relationship(
        "Booking",
        backref=backref("boarding_pass_booking", cascade="all, delete-orphan"),
        foreign_keys=[booking_id]
    )

    def __repr__(self) -> str:
        return "<BoardingPass %r>" % self.id

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self)


class Passenger(Base):
    __tablename__ = "passenger"
    id = Column(BigInteger, primary_key=True, autoincrement="auto")
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    country_of_citizenship = Column(String(50), nullable=False)
    country_of_residence = Column(String(50), nullable=False)
    passport_number = Column(String(20), nullable=False, unique=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now(), nullable=True)

    def __repr__(self) -> str:
        return '<Passenger %r>' % self.passport_number

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self)


class NoFlyList(Base):
    __tablename__ = "noflylist"
    id = Column(BigInteger, primary_key=True, autoincrement="auto")
    active_from = Column(Date, nullable=False)
    active_to = Column(Date, nullable=False)
    nf_reason = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now(), nullable=True)
    passenger_id = Column(BigInteger, ForeignKey('passenger.id'), nullable=False)
    psgnr = relationship(
        "Passenger",
        backref=backref("noflylist", cascade="all, delete-orphan"),
        foreign_keys=[passenger_id]
    )

    def __repr__(self) -> str:
        return "<NoFlyList %r>" % self.id

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self)


class Booking(Base):
    __tablename__ = "booking"
    id = Column(BigInteger, primary_key=True, autoincrement="auto")
    flight_id = Column(BigInteger)
    status = Column(String(20), nullable=False)
    booking_platform = Column(String(20), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now(), nullable=True)
    passenger_id = Column(BigInteger, ForeignKey('passenger.id'), nullable=False)
    passenger = relationship(
        "Passenger",
        backref=backref("booking_passenger", cascade="all, delete-orphan"),
        foreign_keys=[passenger_id]
    )

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self)


class Baggage(Base):
    __tablename__ = "baggage"
    id = Column(BigInteger, primary_key=True, autoincrement="auto")
    weight_in_kg = Column(DECIMAL(4, 2))
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now(), nullable=True)
    booking_id = Column(BigInteger, ForeignKey('booking.id'), nullable=False)
    booking = relationship(
        "Booking",
        backref=backref("baggage_booking", cascade="all, delete-orphan"),
        foreign_keys=[booking_id]
    )

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self)


class SecurityCheck(Base):
    __tablename__ = "security_check"
    id = Column(BigInteger, primary_key=True, autoincrement="auto")
    check_result = Column(String(20), nullable=False)
    comments = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now(), nullable=True)
    passenger_id = Column(BigInteger, ForeignKey('passenger.id'), nullable=False)
    passenger = relationship(
        "Passenger",
        backref=backref("security_check_passenger", cascade="all, delete-orphan"),
        foreign_keys=[passenger_id]
    )

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self)


class BaggageCheck(Base):
    __tablename__ = "baggage_check"
    id = Column(BigInteger, primary_key=True, autoincrement="auto")
    check_result = Column(String(50), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now(), nullable=True)
    passenger_id = Column(BigInteger, ForeignKey('passenger.id'))
    passenger = relationship(
        "Passenger",
        backref=backref("baggage_check_passenger", cascade="all, delete-orphan"),
        uselist=False,
        foreign_keys=[passenger_id]
    )
    booking_id = Column(BigInteger, ForeignKey('booking.id'), nullable=False)
    booking = relationship(
        "Booking",
        backref=backref("baggage_check_booking", cascade="all, delete-orphan"),
        foreign_keys=[booking_id]
    )

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self)


class FlightManifest(Base):
    __tablename__ = "flight_manifest"
    id = Column(BigInteger, primary_key=True, autoincrement="auto")
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now(), nullable=True)
    booking_id = Column(BigInteger, ForeignKey('booking.id'), nullable=False)
    booking = relationship(
        "Booking",
        backref=backref("flight_manifest_booking", cascade="all, delete-orphan"),
        foreign_keys=[booking_id]
    )
    flight_id = Column(BigInteger, ForeignKey('flight.id'), nullable=False)
    flight = relationship(
        "Flight",
        backref=backref("flight_manifest_flight", cascade="all, delete-orphan"),
        foreign_keys=[flight_id]
    )

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self)


Base.metadata.create_all(engine)
