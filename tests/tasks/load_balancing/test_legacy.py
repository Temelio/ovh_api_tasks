"""
'lb.legacy' namespace tasks tests
"""

import re
import sys

from invoke import MockContext
from invoke.exceptions import ParseError
import ovh
import pytest
from spec import trap

from ovh_api_tasks.tasks.load_balancing import legacy as lb_legacy_tasks


@trap
def test_get_legacy_lb_empty(mocker):
    """
    Test lb.legacy.list task without service returned by API
    """

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.get_ip_lb_services', return_value=[])
    lb_legacy_tasks.get_legacy_lb(MockContext())

    output = sys.stdout.getvalue()

    assert re.search(
        r'Service name\s*Zone\s*Load Balancing IP\s*Backends\s*State', output)
    assert re.search('Expired services', output)


@trap
def test_get_legacy_lb_not_empty(
        mocker, ip_load_balancing_array, ip_load_balancing_ip, ip_block_array,
        service_expired):
    """
    Test lb.legacy.list task with some services returned by API
    """

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.get_ip_lb_services',
        return_value=ip_load_balancing_array)

    ip_load_balancing_services = [
        ip_load_balancing_ip,
        service_expired
    ]

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.get_ip_lb_service',
        side_effect=ip_load_balancing_services)

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.get_ip_lb_service_backends',
        return_result=ip_block_array)

    lb_legacy_tasks.get_legacy_lb(MockContext())

    output = sys.stdout.getvalue()

    assert re.search(
        r'Service name\s*Zone\s*Load Balancing IP\s*Backends\s*State', output)
    assert re.search('Expired services', output)


@trap
def test_get_legacy_lb_error(mocker, ip_load_balancing_array):
    """
    Test lb.legacy.list task with some services returned by API
    """

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.get_ip_lb_services',
        return_value=ip_load_balancing_array)

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.get_ip_lb_service',
        return_value=ovh.exceptions.APIError())

    with pytest.raises(ovh.exceptions.APIError):
        lb_legacy_tasks.get_legacy_lb(MockContext())

    output = sys.stdout.getvalue()

    assert output == ''


@trap
def test_add_legacy_lb_backend_bad_service(mocker, ip_load_balancing_array):  # pylint: disable=invalid-name
    """
    Test lb.legacy.add-backend task with bad service
    """

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.get_ip_lb_services',
        return_value=ip_load_balancing_array)

    with pytest.raises(ParseError):
        lb_legacy_tasks.add_backend_to_legacy_lb(
            MockContext(), '10.0.0.5', 'ip-10.0.0.10', 'http')

    output = sys.stdout.getvalue()
    error = sys.stderr.getvalue()

    assert output == ''
    assert error == ''


@trap
def test_add_legacy_lb_backend_error(mocker, ip_load_balancing_array):  # pylint: disable=invalid-name
    """
    Test lb.legacy.add-backend task with error
    """

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.get_ip_lb_services',
        return_value=ip_load_balancing_array)

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.get_ip_lb_service_backends',
        side_effect=[['10.0.0.4'], ['10.0.0.5']])

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.add_ip_lb_service_backend',
        side_effect=ovh.exceptions.APIError('Force test error'))

    lb_legacy_tasks.add_backend_to_legacy_lb(
        MockContext(), '10.0.0.5', 'ip-10.0.0.1,ip-10.0.0.2', 'http')

    output = sys.stdout.getvalue()
    error = sys.stderr.getvalue()

    assert 'ERROR - Add 10.0.0.5 to ip-10.0.0.1 : Force test error' in output
    assert 'INFO - Backend 10.0.0.5 already linked to ip-10.0.0.2' in output
    assert error == ''


@trap
def test_add_legacy_lb_backend(mocker, ip_load_balancing_array, ip_lb_task_add_backend):
    """
    Test lb.legacy.add-backend task without error
    """

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.get_ip_lb_services',
        return_value=ip_load_balancing_array)

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.get_ip_lb_service_backends',
        side_effect=[['10.0.0.4'], ['10.0.0.5']])

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.add_ip_lb_service_backend',
        return_value=ip_lb_task_add_backend)

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.get_ip_lb_service_tasks',
        side_effect=[[ip_lb_task_add_backend], []])

    lb_legacy_tasks.add_backend_to_legacy_lb(
        MockContext(), '10.0.0.5', 'ip-10.0.0.1,ip-10.0.0.2', 'http')

    output = sys.stdout.getvalue().strip().split('\n')
    error = sys.stderr.getvalue()

    assert output[0] == 'INFO - Link "10.0.0.5" to "ip-10.0.0.1" : task 1234'
    assert 'ip-10.0.0.1 - 1 task(s) in progress' in output[1]
    assert "'creationDate': '2017-01-01 12:00:00'" in output[1]
    assert "'status': 'in progress'" in output[1]
    assert "action': 'addBackend'" in output[1]
    assert "'id': '1234'" in output[1]
    assert output[2] == '  ip-10.0.0.1 - All tasks done'
    assert output[3] == 'INFO - Backend 10.0.0.5 already linked to ip-10.0.0.2'
    assert error == ''


@trap
def test_remove_legacy_lb_backend_bad_service(mocker, ip_load_balancing_array):  # pylint: disable=invalid-name
    """
    Test lb.legacy.del-backend task with bad service
    """

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.get_ip_lb_services',
        return_value=ip_load_balancing_array)

    with pytest.raises(ParseError):
        lb_legacy_tasks.remove_backend_from_legacy_lb(
            MockContext(), '10.0.0.5', 'ip-10.0.0.10')

    output = sys.stdout.getvalue()
    error = sys.stderr.getvalue()

    assert output == ''
    assert error == ''


@trap
def test_remove_legacy_lb_backend_error(mocker, ip_load_balancing_array):  # pylint: disable=invalid-name
    """
    Test lb.legacy.remove-backend task with error
    """

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.get_ip_lb_services',
        return_value=ip_load_balancing_array)

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.get_ip_lb_service_backends',
        side_effect=[['10.0.0.4'], ['10.0.0.5']])

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.delete_ip_lb_service_backend',
        side_effect=ovh.exceptions.APIError('Force test error'))

    lb_legacy_tasks.remove_backend_from_legacy_lb(
        MockContext(), '10.0.0.5', 'ip-10.0.0.1,ip-10.0.0.2')

    output = sys.stdout.getvalue()
    error = sys.stderr.getvalue()

    assert 'INFO - Backend 10.0.0.5 not linked to ip-10.0.0.1' in output
    assert 'ERROR - Remove 10.0.0.5 from ip-10.0.0.2 : Force test error' in output
    assert error == ''


@trap
def test_remove_legacy_lb_backend(mocker, ip_load_balancing_array, ip_lb_task_del_backend):
    """
    Test lb.legacy.remove-backend task without error
    """

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.get_ip_lb_services',
        return_value=ip_load_balancing_array)

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.get_ip_lb_service_backends',
        side_effect=[['10.0.0.4'], ['10.0.0.5']])

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.delete_ip_lb_service_backend',
        return_value=ip_lb_task_del_backend)

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.get_ip_lb_service_tasks',
        side_effect=[[ip_lb_task_del_backend], []])

    lb_legacy_tasks.remove_backend_from_legacy_lb(
        MockContext(), '10.0.0.5', 'ip-10.0.0.1,ip-10.0.0.2')

    output = sys.stdout.getvalue().strip().split('\n')
    error = sys.stderr.getvalue()

    assert output[0] == 'INFO - Backend 10.0.0.5 not linked to ip-10.0.0.1'
    assert output[1] == 'INFO - Unlink "10.0.0.5" from "ip-10.0.0.2" : task 1234'
    assert 'ip-10.0.0.2 - 1 task(s) in progress' in output[2]
    assert "'creationDate': '2017-01-01 12:00:00'" in output[2]
    assert "'status': 'in progress'" in output[2]
    assert "action': 'delBackend'" in output[2]
    assert "'id': '1234'" in output[2]
    assert output[3] == '  ip-10.0.0.2 - All tasks done'
    assert error == ''
