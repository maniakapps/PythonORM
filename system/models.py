from sqlalchemy import Column, String, DateTime, BigInteger, Text, Date, DECIMAL, create_engine, MetaData, ForeignKey, \
    func
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Airport(Base):
    """Airport class
    """
    __tablename__ = "airport"
    a_id = Column(BigInteger, primary_key=True, autoincrement="auto")
    airport_name = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self) -> str:
        return "<Airport %r>" % self.airport_name


class Flight(Base):
    """Flight class"""
    __tablename__ = "flight"
    flight_id = Column(BigInteger, primary_key=True)
    departing_gate = Column(String(20), nullable=False)
    arriving_gate = Column(String(20), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    airline_id = Column(BigInteger, ForeignKey('airline.airline_id'))
    airline = relationship(
        "Airline",
        back_populates="flight",
        cascade="all, delete-orphan"
    )
    departing_airport_id = Column(BigInteger, ForeignKey('airline.airline_id'))
    departing_airport = relationship(
        "Airport",
        back_populates="flight",
        cascade="all, delete-orphan"
    )
    arriving_airport_id = Column(BigInteger, ForeignKey('airline.airline_id'))
    arriving_airport = relationship(
        "Airport",
        back_populates="flight",
        cascade="all, delete-orphan"
    )


class Airline(Base):
    __tablename__ = "airline"
    airline_id = Column(BigInteger, primary_key=True)
    airline_code = Column(String, nullable=False)
    airline_name = Column(String, nullable=False)
    airline_country = Column(String(50), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())


class BoardingPass(Base):
    __tablename__ = "boarding_pass"
    boarding_pass_id = Column(BigInteger, primary_key=True)
    qr_code = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    booking_id = Column(BigInteger, ForeignKey('booking.booking_id'))
    booking = relationship(
        "Booking",
        back_populates="boarding_pass",
        cascade="all, delete-orphan"
    )


class Passenger(Base):
    __tablename__ = "passenger"
    passenger_id = Column(BigInteger, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    country_of_citizenship = Column(String(50), nullable=False)
    country_of_residence = Column(String(50), nullable=False)
    passport_number = Column(String(20), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())


class NoFlyList(Base):
    __tablename__ = "noflylist"
    nf_id = Column(BigInteger, primary_key=True)
    active_from = Column(Date, nullable=False)
    active_to = Column(Date, nullable=False)
    nf_reason = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    passenger_id = Column(BigInteger, ForeignKey('passenger.passenger_id'))
    psgnr = relationship(
        "Passenger",
        back_populates="noflylist",
        cascade="all, delete-orphan"
    )


class Booking(Base):
    __tablename__ = "booking"
    booking_id = Column(BigInteger, primary_key=True)
    flight_id = Column(BigInteger)
    status = Column(String(20), nullable=False)
    booking_platform = Column(String(20), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    passenger_id = Column(BigInteger, ForeignKey('passenger.passenger_id'))
    passenger = relationship(
        "Passenger",
        back_populates="booking",
        cascade="all, delete-orphan"
    )


class Baggage(Base):
    __tablename__ = "baggage"
    baggage_id = Column(BigInteger, primary_key=True)
    weight_in_kg = Column(DECIMAL(4, 2))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    booking_id = Column(BigInteger, ForeignKey('booking.booking_id'))
    booking = relationship(
        "Booking",
        back_populates="baggage",
        cascade="all, delete-orphan"
    )


class SecurityCheck(Base):
    __tablename__ = "security_check"
    security_id = Column(BigInteger, primary_key=True)
    check_result = Column(String(20), nullable=False)
    comments = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    passenger_id = Column(BigInteger, ForeignKey('passenger.passenger_id'))
    passenger = relationship(
        "Passenger",
        back_populates="security_check",
        cascade="all, delete-orphan"
    )


class BaggageCheck(Base):
    __tablename__ = "baggage_check"
    baggage_check_id = Column(BigInteger, primary_key=True)
    check_result = Column(String(50), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    passenger_id = Column(BigInteger, ForeignKey('passenger.passenger_id'))
    passenger = relationship(
        "Passenger",
        back_populates="baggage_check",
        cascade="all, delete-orphan"
    )
    booking_id = Column(BigInteger, ForeignKey('booking.booking_id'))
    booking = relationship(
        "Booking",
        back_populates="baggage_check",
        cascade="all, delete-orphan"
    )


class FlightManifest(Base):
    __tablename__ = "flight_manifest"
    flight_manifest_id = Column(BigInteger, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    booking_id = relationship(
        "Booking",
        back_populates="flight_manifest",
        cascade="all, delete-orphan"
    )
    flight_id = Column(BigInteger, ForeignKey('flight.flight_id'))
    flight = relationship(
        "Flight",
        back_populates="flight_manifest",
        cascade="all, delete-orphan"
    )
