# (c) Tiago Tamagusko 2022
"""Transforms an address into coordinates.

Example:
    # Get the coordinates of Berlin.
    get_coordinates('Berlin, Germany')
    Return:
        (52.5170365, 13.3888599)
"""
from __future__ import annotations

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable, GeocoderTimedOut


def get_coordinates(address: str):
    """Return coordinates (lat, lon) of address.

    Args:
        address: Country, city, street, continent, etc.

    Returns:
        latitude, longitude or None if unavailable
    """
    locator = Nominatim(user_agent="myGeocode", timeout=10)
    try:
        location = locator.geocode(address)
        if location:
            return location.latitude, location.longitude
        return None  # If the address is not found, return None
    except (AttributeError, GeocoderUnavailable, GeocoderTimedOut):
        return None  # If geocoding fails for any reason, return None
