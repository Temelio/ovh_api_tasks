"""
/ip API wrapper tests
"""

import ovh

from ovh_api_tasks.api_wrappers import ip


# Pylint not manage properly dynamic stuff like 'mock' package use
# pylint: disable=no-member

def test_get_ips(mocker):
    """
    Test get_ips function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip.get_ips(ovh_client)
    ovh_client.call.assert_called_with('GET', '/ip', None, True)


def test_get_ip(mocker):
    """
    Test get_ip function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip.get_ip(ovh_client, '1.2.3.4')
    ovh_client.call.assert_called_with('GET', '/ip/1.2.3.4', None, True)


def test_get_ip_lb_services(mocker):
    """
    Test get_ip_lb_services function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip.get_ip_lb_services(ovh_client)
    ovh_client.call.assert_called_with('GET', '/ip/loadBalancing', None, True)


def test_get_ip_lb_service(mocker):
    """
    Test get_ip_lb_service_details function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip.get_ip_lb_service(ovh_client, 'test-service')
    ovh_client.call.assert_called_with(
        'GET', '/ip/loadBalancing/test-service', None, True)


def test_get_ip_lb_service_backends(mocker):
    """
    Test get_ip_lb_service_backends function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip.get_ip_lb_service_backends(ovh_client, 'test-service')
    ovh_client.call.assert_called_with(
        'GET', '/ip/loadBalancing/test-service/backend', None, True)


def test_get_ip_lb_service_backend(mocker):
    """
    Test get_ip_lb_service_backend function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip.get_ip_lb_service_backend(ovh_client, 'test-service', 'test-backend')
    ovh_client.call.assert_called_with(
        'GET',
        '/ip/loadBalancing/test-service/backend/test-backend',
        None,
        True)


def test_add_ip_lb_service_backend(mocker):
    """
    Test add_ip_lb_service_backend function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip.add_ip_lb_service_backend(
        ovh_client, 'test-service', 'test-backend', 'http')

    ovh_client.call.assert_called_with(
        'POST',
        '/ip/loadBalancing/test-service/backend',
        {'ipBackend': 'test-backend', 'probe': 'http'},
        True
    )


def test_delete_ip_lb_service_backend(mocker):  # pylint: disable=invalid-name
    """
    Test delete_ip_lb_service_backend function
    """

    mocker.patch('ovh.client.Client.call', return_value={'id': 12})
    ovh_client = ovh.Client()

    ip.delete_ip_lb_service_backend(ovh_client, 'test-service', 'test-backend')

    ovh_client.call.assert_called_with(
        'DELETE',
        '/ip/loadBalancing/test-service/backend/test-backend',
        None,
        True
    )


def test_get_ip_lb_service_tasks(mocker):
    """
    Test get_ip_lb_service_tasks function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip.get_ip_lb_service_tasks(ovh_client, 'test-service')
    ovh_client.call.assert_called_with(
        'GET', '/ip/loadBalancing/test-service/task', None, True)


def test_get_ip_lb_service_task(mocker):
    """
    Test get_ip_lb_service_task_details function
    """

    mocker.patch('ovh.client.Client.call')
    ovh_client = ovh.Client()

    ip.get_ip_lb_service_task(ovh_client, 'test-service', 'test-task')
    ovh_client.call.assert_called_with(
        'GET',
        '/ip/loadBalancing/test-service/task/test-task',
        None,
        True)
