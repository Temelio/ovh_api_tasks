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


def test_get_ip_lb_service_http_farms(mocker):  # pylint: disable=invalid-name
    """
    Test get_ip_lb_service_http_farms function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_http_farms(ovh_client, 'ip-10.0.0.1')
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/http/farm', None, True)


def test_get_ip_lb_service_http_farms_with_params(mocker):  # pylint: disable=invalid-name
    """
    Test get_ip_lb_service_http_farms function with zone param
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_http_farms(ovh_client, 'ip-10.0.0.1', zone='foo')
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/http/farm?zone=foo', None, True)


def test_get_ip_lb_service_http_farm(mocker):  # pylint: disable=invalid-name
    """
    Test get_ip_lb_service_http_farm function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_http_farm(ovh_client, 'ip-10.0.0.1', 1234)
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/http/farm/1234', None, True)


def test_add_ip_lb_service_http_farm(mocker):  # pylint: disable=invalid-name
    """
    Test add_ip_lb_service_http_farm function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.add_ip_lb_service_http_farm(ovh_client, 'ip-10.0.0.1', {'foo':'bar'})
    ovh_client.call.assert_called_with(
        'POST', '/ipLoadbalancing/ip-10.0.0.1/http/farm', {'foo': 'bar'}, True)


def test_del_ip_lb_service_http_farm(mocker):  # pylint: disable=invalid-name
    """
    Test del_ip_lb_service_http_farm function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.del_ip_lb_service_http_farm(ovh_client, 'ip-10.0.0.1', 1234)
    ovh_client.call.assert_called_with(
        'DELETE', '/ipLoadbalancing/ip-10.0.0.1/http/farm/1234', None, True)


def test_get_ip_lb_service_http_farm_servers(mocker):  # pylint: disable=invalid-name
    """
    Test get_ip_lb_service_http_farm_servers function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_http_farm_servers(ovh_client, 'ip-10.0.0.1', 1234)
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/http/farm/1234/server', None, True)


def test_get_ip_lb_service_http_farm_server(mocker):  # pylint: disable=invalid-name
    """
    Test get_ip_lb_service_http_farm_server function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_http_farm_server(ovh_client, 'ip-10.0.0.1', 1234, 5678)
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/http/farm/1234/server/5678', None, True)


def test_add_ip_lb_service_http_farm_server(mocker):  # pylint: disable=invalid-name
    """
    Test add_ip_lb_service_http_farm_server function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.add_ip_lb_service_http_farm_server(ovh_client, 'ip-10.0.0.1', 1234, {'foo':'bar'})
    ovh_client.call.assert_called_with(
        'POST', '/ipLoadbalancing/ip-10.0.0.1/http/farm/1234/server', {'foo': 'bar'}, True)


def test_update_ip_lb_service_http_farm_server(mocker):  # pylint: disable=invalid-name
    """
    Test update_ip_lb_service_http_farm_server function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.update_ip_lb_service_http_farm_server(
        ovh_client, 'ip-10.0.0.1', 1234, 5678, {'foo':'bar'})
    ovh_client.call.assert_called_with(
        'PUT', '/ipLoadbalancing/ip-10.0.0.1/http/farm/1234/server/5678', {'foo': 'bar'}, True)


def test_del_ip_lb_service_http_farm_server(mocker):  # pylint: disable=invalid-name
    """
    Test del_ip_lb_service_http_farm_server function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.del_ip_lb_service_http_farm_server(ovh_client, 'ip-10.0.0.1', 1234, 5678)
    ovh_client.call.assert_called_with(
        'DELETE', '/ipLoadbalancing/ip-10.0.0.1/http/farm/1234/server/5678', None, True)


def test_get_ip_lb_service_http_frontends(mocker):  # pylint: disable=invalid-name
    """
    Test get_ip_lb_service_http_frontends function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_http_frontends(ovh_client, 'ip-10.0.0.1')
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/http/frontend', None, True)


def test_get_ip_lb_service_http_frontend(mocker):  # pylint: disable=invalid-name
    """
    Test get_ip_lb_service_http_frontend function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_http_frontend(ovh_client, 'ip-10.0.0.1', 1234)
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/http/frontend/1234', None, True)


def test_add_ip_lb_service_http_frontend(mocker):  # pylint: disable=invalid-name
    """
    Test add_ip_lb_service_http_frontend function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.add_ip_lb_service_http_frontend(ovh_client, 'ip-10.0.0.1', {'foo':'bar'})
    ovh_client.call.assert_called_with(
        'POST', '/ipLoadbalancing/ip-10.0.0.1/http/frontend', {'foo': 'bar'}, True)


def test_del_ip_lb_service_http_frontend(mocker):  # pylint: disable=invalid-name
    """
    Test del_ip_lb_service_http_frontend function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.del_ip_lb_service_http_frontend(ovh_client, 'ip-10.0.0.1', 1234)
    ovh_client.call.assert_called_with(
        'DELETE', '/ipLoadbalancing/ip-10.0.0.1/http/frontend/1234', None, True)


def test_get_ip_lb_service_tcp_farms(mocker):  # pylint: disable=invalid-name
    """
    Test get_ip_lb_service_tcp_farms function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_tcp_farms(ovh_client, 'ip-10.0.0.1')
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/tcp/farm', None, True)


def test_get_ip_lb_service_tcp_farms_with_params(mocker):  # pylint: disable=invalid-name
    """
    Test get_ip_lb_service_tcp_farms function with zone param
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_tcp_farms(ovh_client, 'ip-10.0.0.1', zone='foo')
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/tcp/farm?zone=foo', None, True)


def test_get_ip_lb_service_tcp_farm(mocker):  # pylint: disable=invalid-name
    """
    Test get_ip_lb_service_tcp_farm function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_tcp_farm(ovh_client, 'ip-10.0.0.1', 1234)
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/tcp/farm/1234', None, True)


def test_add_ip_lb_service_tcp_farm(mocker):  # pylint: disable=invalid-name
    """
    Test add_ip_lb_service_tcp_farm function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.add_ip_lb_service_tcp_farm(ovh_client, 'ip-10.0.0.1', {'foo':'bar'})
    ovh_client.call.assert_called_with(
        'POST', '/ipLoadbalancing/ip-10.0.0.1/tcp/farm', {'foo': 'bar'}, True)


def test_del_ip_lb_service_tcp_farm(mocker):  # pylint: disable=invalid-name
    """
    Test del_ip_lb_service_tcp_farm function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.del_ip_lb_service_tcp_farm(ovh_client, 'ip-10.0.0.1', 1234)
    ovh_client.call.assert_called_with(
        'DELETE', '/ipLoadbalancing/ip-10.0.0.1/tcp/farm/1234', None, True)


def test_get_ip_lb_service_tcp_farm_servers(mocker):  # pylint: disable=invalid-name
    """
    Test get_ip_lb_service_tcp_farm_servers function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_tcp_farm_servers(ovh_client, 'ip-10.0.0.1', 1234)
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/tcp/farm/1234/server', None, True)


def test_get_ip_lb_service_tcp_farm_server(mocker):  # pylint: disable=invalid-name
    """
    Test get_ip_lb_service_tcp_farm_server function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_tcp_farm_server(ovh_client, 'ip-10.0.0.1', 1234, 5678)
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/tcp/farm/1234/server/5678', None, True)


def test_add_ip_lb_service_tcp_farm_server(mocker):  # pylint: disable=invalid-name
    """
    Test add_ip_lb_service_tcp_farm_server function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.add_ip_lb_service_tcp_farm_server(ovh_client, 'ip-10.0.0.1', 1234, {'foo':'bar'})
    ovh_client.call.assert_called_with(
        'POST', '/ipLoadbalancing/ip-10.0.0.1/tcp/farm/1234/server', {'foo': 'bar'}, True)


def test_update_ip_lb_service_tcp_farm_server(mocker):  # pylint: disable=invalid-name
    """
    Test update_ip_lb_service_tcp_farm_server function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.update_ip_lb_service_tcp_farm_server(
        ovh_client, 'ip-10.0.0.1', 1234, 5678, {'foo':'bar'})
    ovh_client.call.assert_called_with(
        'PUT', '/ipLoadbalancing/ip-10.0.0.1/tcp/farm/1234/server/5678', {'foo': 'bar'}, True)


def test_del_ip_lb_service_tcp_farm_server(mocker):  # pylint: disable=invalid-name
    """
    Test del_ip_lb_service_tcp_farm_server function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.del_ip_lb_service_tcp_farm_server(ovh_client, 'ip-10.0.0.1', 1234, 5678)
    ovh_client.call.assert_called_with(
        'DELETE', '/ipLoadbalancing/ip-10.0.0.1/tcp/farm/1234/server/5678', None, True)


def test_get_ip_lb_service_tcp_frontends(mocker):  # pylint: disable=invalid-name
    """
    Test get_ip_lb_service_tcp_frontends function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_tcp_frontends(ovh_client, 'ip-10.0.0.1')
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/tcp/frontend', None, True)


def test_get_ip_lb_service_tcp_frontend(mocker):  # pylint: disable=invalid-name
    """
    Test get_ip_lb_service_tcp_frontend function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_tcp_frontend(ovh_client, 'ip-10.0.0.1', 1234)
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/tcp/frontend/1234', None, True)


def test_add_ip_lb_service_tcp_frontend(mocker):  # pylint: disable=invalid-name
    """
    Test add_ip_lb_service_tcp_frontend function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.add_ip_lb_service_tcp_frontend(ovh_client, 'ip-10.0.0.1', {'foo':'bar'})
    ovh_client.call.assert_called_with(
        'POST', '/ipLoadbalancing/ip-10.0.0.1/tcp/frontend', {'foo': 'bar'}, True)


def test_del_ip_lb_service_tcp_frontend(mocker):  # pylint: disable=invalid-name
    """
    Test del_ip_lb_service_tcp_frontend function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.del_ip_lb_service_tcp_frontend(ovh_client, 'ip-10.0.0.1', 1234)
    ovh_client.call.assert_called_with(
        'DELETE', '/ipLoadbalancing/ip-10.0.0.1/tcp/frontend/1234', None, True)


def test_refresh_ip_lb_service(mocker):  # pylint: disable=invalid-name
    """
    Test refresh_ip_lb_service function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.refresh_ip_lb_service(ovh_client, 'ip-10.0.0.1')
    ovh_client.call.assert_called_with(
        'POST', '/ipLoadbalancing/ip-10.0.0.1/refresh', {'zone': None}, True)


def test_get_ip_lb_service_ssl_items(mocker):  # pylint: disable=invalid-name
    """
    Test get_ip_lb_service_ssl_items function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_ssl_items(ovh_client, 'ip-10.0.0.1')
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/ssl', None, True)


def test_get_ip_lb_service_ssl_item(mocker):  # pylint: disable=invalid-name
    """
    Test get_ip_lb_service_ssl_item function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.get_ip_lb_service_ssl_item(ovh_client, 'ip-10.0.0.1', 1234)
    ovh_client.call.assert_called_with(
        'GET', '/ipLoadbalancing/ip-10.0.0.1/ssl/1234', None, True)


def test_add_ip_lb_service_ssl_item(mocker):  # pylint: disable=invalid-name
    """
    Test add_ip_lb_service_ssl_item function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.add_ip_lb_service_ssl_item(ovh_client, 'ip-10.0.0.1', {'foo':'bar'})
    ovh_client.call.assert_called_with(
        'POST', '/ipLoadbalancing/ip-10.0.0.1/ssl', {'foo': 'bar'}, True)


def test_del_ip_lb_service_ssl_item(mocker):  # pylint: disable=invalid-name
    """
    Test del_ip_lb_service_ssl_item function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip_lb.del_ip_lb_service_ssl_item(ovh_client, 'ip-10.0.0.1', 1234)
    ovh_client.call.assert_called_with(
        'DELETE', '/ipLoadbalancing/ip-10.0.0.1/ssl/1234', None, True)
