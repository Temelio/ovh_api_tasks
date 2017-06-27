"""
'ip' namespace tasks tests
"""

import re
import sys

import ovh
import pytest
from invoke import MockContext
from spec import trap

from ovh_api_tasks.tasks import ip as ip_tasks


@trap
def test_get_ips_empty(mocker):
    """
    Test ip.get_ips task without IP returned by API
    """

    mocker.patch('ovh_api_tasks.api_wrappers.ip.get_ips', return_value=[])
    ip_tasks.get_ips(MockContext())

    output = sys.stdout.getvalue()

    assert re.search(r'Type\s*Service name\s*IP blocks', output)
    assert re.search('Expired IP blocks', output)


@trap
def test_get_ips_not_empty(
        mocker, ip_block_array, ip_v4, ip_v6, service_expired):
    """
    Test ip.get_ips task with some IPs returned by API
    """

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.get_ips', return_value=ip_block_array)

    get_ip_responses = [ip_v4, ip_v6, service_expired]

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.get_ip', side_effect=get_ip_responses)

    ip_tasks.get_ips(MockContext())
    output = sys.stdout.getvalue()

    assert re.search(r'Type\s*Service name\s*IP blocks', output)
    assert re.search(r'dedicated\s*foo\s*10.0.0.1/32', output)
    assert re.search(r'vps\s*bar\s*fd2e:c4d1:8a4b:d6f7::/64', output)
    assert re.search(r'Expired IP blocks\s*-*\s*10.0.0.3$', output)


@trap
def test_get_ips_error(mocker, ip_block_array):
    """
    Test ip.get_ips task with unexpected API error
    """

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.get_ips', return_value=ip_block_array)

    mocker.patch(
        'ovh_api_tasks.api_wrappers.ip.get_ip',
        side_effect=ovh.exceptions.APIError('Test unexpected error'))

    with pytest.raises(ovh.exceptions.APIError) as error:
        ip_tasks.get_ips(MockContext())

    assert 'Test unexpected error' in str(error)
