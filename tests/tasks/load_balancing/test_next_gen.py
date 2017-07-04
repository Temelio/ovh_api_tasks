"""
'lb.next-gen' namespace tasks tests
"""

import re
import sys

from invoke import MockContext
from invoke.exceptions import ParseError
import ovh
import pytest
from spec import trap

from ovh_api_tasks.tasks.load_balancing import next_gen as lb_ng_tasks


@trap
def test_get_ng_lb_empty(mocker):
    """
    Test lb.next_gen.list task without service returned by API
    """

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip_loadbalancing.get_ip_lb_services',
        return_value=[])
    lb_ng_tasks.get_next_gen_lb(MockContext())

    output = sys.stdout.getvalue()

    assert re.search(
        r"""Service\ name\s+Zone\s+Load\ Balancing\ IP\s+IPv6\s+Farms\s+
            SSL\ configuration\s+Display\ name\s+State\s+Offer""",
        output,
        re.VERBOSE)
    assert re.search('Expired services', output)


@trap
def test_get_ng_lb_not_empty(
        mocker, ip_lb_array, ip_lb, ip_lb_farm_array, service_expired):
    """
    Test lb.next_gen.list task with some services returned by API
    """

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip_loadbalancing.get_ip_lb_services',
        return_value=ip_lb_array)

    ip_lb_services = [
        ip_lb,
        service_expired
    ]

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip_loadbalancing.get_ip_lb_service',
        side_effect=ip_lb_services)

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip_loadbalancing.get_ip_lb_service_farms',
        return_result=ip_lb_farm_array)

    lb_ng_tasks.get_next_gen_lb(MockContext())

    output = sys.stdout.getvalue()

    assert re.search(
        r"""Service\ name\s+Zone\s+Load\ Balancing\ IP\s+IPv6\s+Farms\s+
            SSL\ configuration\s+Display\ name\s+State\s+Offer""",
        output,
        re.VERBOSE)
    assert re.search('Expired services', output)


@trap
def test_get_ng_lb_error(mocker, ip_lb_array):
    """
    Test lb.next_gen.list task with error returned by API
    """

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip_loadbalancing.get_ip_lb_services',
        return_value=ip_lb_array)

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip_loadbalancing.get_ip_lb_service',
        return_value=ovh.exceptions.APIError())

    with pytest.raises(ovh.exceptions.APIError):
        lb_ng_tasks.get_next_gen_lb(MockContext())

    output = sys.stdout.getvalue()

    assert output == ''


@trap
def test_get_ng_lb_http_farms(
        mocker, ip_lb_farm_array, ip_lb_http_farm):
    """
    Test lb.next_gen.http-farms task with some services returned by API
    """

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip_loadbalancing.get_ip_lb_service_http_farms',
        return_value=ip_lb_farm_array)

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip_loadbalancing.get_ip_lb_service_http_farm',
        return_value=ip_lb_http_farm)

    lb_ng_tasks.get_next_gen_lb_http_farm(MockContext(), 'ip-10.0.0.1')

    output = sys.stdout.getvalue()

    assert re.search(
        r"""Service\ name\s+Display\ name\s+Farm\ ID\s+Balance\s+Zone\s+
            Port\s+Probe\s+Stickiness""",
        output,
        re.VERBOSE)
