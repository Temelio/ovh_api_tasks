"""
Exceptions fixtures
"""

from ovh.exceptions import APIError
import pytest


@pytest.fixture()
def service_expired():
    """
    Raise an OVH exception same as an expired service
    """

    return APIError('This service is expired')
