"""
IP wrappers fixtures
"""

import pytest


@pytest.fixture()
def ip_block_array():
    """
    Return an ipBlock array instance fixture
    """

    return ['10.0.0.1', '10.0.0.2', '10.0.0.3']


@pytest.fixture()
def ip_v4():
    """
    Return an ipBlock array instance fixture
    """

    return {
        'organisationId': None,
        'country': None,
        'routedTo': {
            'serviceName': 'foo'
        },
        'ip': '10.0.0.1/32',
        'canBeTerminated': False,
        'type': 'dedicated',
        'description': None
    }


@pytest.fixture()
def ip_v6():
    """
    Return an ipBlock array instance fixture
    """

    return {
        'organisationId': None,
        'country': None,
        'routedTo': {
            'serviceName': 'bar'
        },
        'ip': 'fd2e:c4d1:8a4b:d6f7::/64',
        'canBeTerminated': False,
        'type': 'vps',
        'description': None
    }
