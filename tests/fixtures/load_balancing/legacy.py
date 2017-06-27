"""
IP wrappers fixtures
"""

import pytest


@pytest.fixture()
def ip_load_balancing_array():
    """
    Return some ip load balancing services
    """

    return ['ip-10.0.0.1', 'ip-10.0.0.2']


@pytest.fixture()
def ip_load_balancing_ip():
    """
    Return an ip load balancing service
    """

    return {
        'ssl': 'none',
        'zone': ['gra'],
        'ipLoadBalancing': '10.0.0.1/32',
        'serviceName': 'ip-10.0.0.1',
        'state': 'ok',
        'stickiness': 'none'
    }
