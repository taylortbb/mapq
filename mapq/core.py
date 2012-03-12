"""
Simplified methods for calling Mapquest's Geocoding API.
"""

from .geo import Geo


def address(name):
    """Geocode an address."""
    return Geo().address(name)


def batch(*locations):
    """Batch geocode multiple addresses."""
    return Geo().batch(*locations)


def geocode(address):
    """Return first the geocode result for a given address."""
    return Geo().address(address)[0]


def latlng(address):
    """Get the latitude and longitude coordinates for an address."""
    return Geo().latlng(address)


def reverse(lat, lng):
    """Reverse geocode lat/lng coordinates."""
    return Geo().reverse(lat, lng)
