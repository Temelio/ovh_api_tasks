"""
Next Gen Load Balancing IP wrappers fixtures
"""

import pytest


@pytest.fixture()
def ip_lb_available_zones():
    """
    Return available zones for IP LB
    """

    return ['rbx', 'gra', 'sbg', 'bhs', 'all']


@pytest.fixture()
def ip_lb_array():
    """
    Return some ip load balancing services
    """

    return ['ip-10.0.0.1', 'ip-10.0.0.2']


@pytest.fixture()
def ip_lb():
    """
    Return an ip load balancing service
    """

    return {
        'ipv6': 'fd2e:c4d1:8a4b:d6f7::/64',
        'metricsToken': 'f5b92a38ac7b4098866fee8c378df0647e9382969665a45261be',
        'zone': ['gra'],
        'offer': 'beta',
        'serviceName': 'ip-10.0.0.1',
        'ipLoadbalancing': '10.0.0.1/32',
        'state': 'ok',
        'sslConfiguration': None,
        'displayName': 'none'
    }


@pytest.fixture()
def ip_lb_farm_array():
    """
    Return ip load balancing farms
    """

    return [
        {
            'type': 'http',
            'id': 1234
        },
        {
            'type': 'http',
            'id': 1235
        },
    ]


@pytest.fixture()
def ip_lb_http_farm():
    """
    Return ip load balancing farm
    """

    return {
        'farmId': 1234,
        'balance': None,
        'zone': 'gra',
        'port': 80,
        'probe': {
            'match': 'status',
            'port': 80,
            'interval': 30,
            'pattern': '204',
            'forceSsl': False,
            'url': '/',
            'type': 'http',
            'method': 'GET'
        },
        'displayName': None,
        'stickiness': None
    }


@pytest.fixture()
def ip_lb_http_farm_servers():
    """
    Return ip load balancing farm servers
    """

    return [
        1234,
        5678
    ]


@pytest.fixture()
def ip_lb_http_farm_server():
    """
    Return ip load balancing farm server
    """

    return {
        'serverState': [],
        'backendId': 55046,
        'status': 'active',
        'ssl': False,
        'cookie': None,
        'port': 80,
        'proxyProtocolVersion': None,
        'chain': '',
        'serverId': 1234,
        'weight': 1,
        'address': '192.168.0.1',
        'backup': False,
        'probe': True,
        'displayName': 'Foo server'
    }


@pytest.fixture()
def ip_lb_http_frontends():
    """
    Return ip load balancing http frontends
    """

    return [
        12345,
        67890
    ]


@pytest.fixture()
def ip_lb_http_frontend():
    """
    Return ip load balancing frontend
    """

    return {
        'defaultSslId': None,
        'disabled': False,
        'zone': 'gra',
        'ssl': False,
        'dedicatedIpfo': None,
        'port': '80',
        'hsts': False,
        'allowedSource': None,
        'httpHeader': None,
        'frontendId': 50486,
        'redirectLocation': None,
        'defaultFarmId': 55046,
        'displayName': None
    }
