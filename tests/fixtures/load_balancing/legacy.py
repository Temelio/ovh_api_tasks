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


@pytest.fixture()
def ip_lb_task_add_backend():
    """
    Return a load balancer task
    """

    return {
        'creationDate': '2017-01-01 12:00:00',
        'status': 'in progress',
        'action': 'addBackend',
        'id': '1234',
    }


@pytest.fixture()
def ip_lb_task_del_backend():
    """
    Return a load balancer task
    """

    return {
        'creationDate': '2017-01-01 12:00:00',
        'status': 'in progress',
        'action': 'delBackend',
        'id': '1234',
    }
