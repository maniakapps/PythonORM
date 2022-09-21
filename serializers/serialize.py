"""Serializers for the objects"""
#  __Author__= "Manuel Pizano"
#  __Email__= "doomclass@proton.me"
#  __Website__= "https://github.com/maniakapps"
#  __Portfolio__= "https://portafoliofullstack.vercel.app/"
#
#  Copyright (c) 2022.

from system.relationships.models import Flight, Booking


def serialize_flight(flight: Flight):
    """Serializes a flight object"""
    return {
        "id": flight.id,
        "departing_gate": flight.departing_gate,
        "arriving_gate": flight.arriving_gate,
        "created_at": flight.created_at,
        "passenger": {
            "id": flight.passenger.id,
            "first_name": flight.passenger.first_name,
            "last_name": flight.passenger.last_name,
            "passport_number": flight.passenger.passport_number
        },
    }


def serialize_booking(booking: Booking):
    """Serializes a booking object"""
    return {
        "id": booking.id,
        "flight_id": booking.flight_id,
        "status": booking.status,
        "booking_platform": booking.booking_platform,
        "created_at": booking.created_at,
        "update_at": booking.updated_at,
        "passenger_id": booking.passenger_id
    }
