"""
/ipLoadbalancing API wrapper tests
"""

import ovh

from ovh_api_tasks.api_wrappers import ip_loadbalancing as ip_lb


# Pylint not manage properly dynamic stuff like 'mock' package use
# pylint: disable=no-member

def test_get_ip_lb_available_zones(mocker):
    """
    Test get_ip_lb_available_zones function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_available_zones(ovh_client)
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/availableZones', None, True)


def test_get_ip_lb_services(mocker):
    """
    Test get_ip_lb_services function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_services(ovh_client)
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing', None, True)


def test_get_ip_lb_service(mocker):
    """
    Test get_ip_lb_service function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service(ovh_client, 'ip-10.0.0.1')
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1', None, True)


def test_get_ip_lb_service_farms(mocker):
    """
    Test get_ip_lb_service_farms function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_farms(ovh_client, 'ip-10.0.0.1')
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/definedFarms', None, True)


def test_get_ip_lb_service_fo_ip(mocker):
    """
    Test get_ip_lb_service_fo_ip function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_fo_ip(ovh_client, 'ip-10.0.0.1')
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/failover', None, True)


def test_get_ip_lb_service_frontends(mocker):  # pylint: disable=invalid-name
    """
    Test get_ip_lb_service_frontends function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_frontends(ovh_client, 'ip-10.0.0.1')
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/definedFrontends', None, True)


def test_get_ip_lb_service_routes(mocker):
    """
    Test get_ip_lb_service_routes function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_routes(ovh_client, 'ip-10.0.0.1')
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/definedRoutes', None, True)


def test_get_ip_lb_instances_state(mocker):
    """
    Test get_ip_lb_service_instance_state function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_instances_state(ovh_client, 'ip-10.0.0.1')
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/instancesState', None, True)


def test_get_ip_lb_nat_ip_subnet(mocker):
    """
    Test get_ip_lb_service_nat_ip_subnet function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_nat_ip_subnet(ovh_client, 'ip-10.0.0.1')
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/natIp', None, True)


def test_get_ip_lb_service_infos(mocker):
    """
    Test get_ip_lb_service_infos function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_infos(ovh_client, 'ip-10.0.0.1')
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/serviceInfos', None, True)


def test_get_ip_lb_service_tasks(mocker):
    """
    Test get_ip_lb_service_tasks function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_tasks(ovh_client, 'ip-10.0.0.1')
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/task', None, True)


def test_get_ip_lb_service_task(mocker):
    """
    Test get_ip_lb_service_tasks function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_task(ovh_client, 'ip-10.0.0.1', 1234)
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/task/1234', None, True)
