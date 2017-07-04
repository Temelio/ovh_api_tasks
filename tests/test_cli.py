#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_ovh_api_tasks
----------------------------------

Tests for `ovh_api_tasks` module.
"""

import re
import sys

import pytest

from spec import trap

from ovh_api_tasks import cli


@trap
def test_cli_tasks():
    """
    Test tasks cli
    """

    with pytest.raises(SystemExit):
        cli.main('ovh-api --list')

    output = sys.stdout.getvalue()
    error = sys.stderr.getvalue()

    tasks_regex = [
        r'ip.ips \(ip\)\s+Return IPs',
        r'lb.legacy.add-backend\s+Add a backend to legacy IP LoadBalancer',
        r'lb.legacy.del-backend\s+Remove a backend from legacy IP LoadBalancer',
        r'lb.legacy.list\s+Return OVH legacy IP LoadBalancers services',
        r'lb.next_gen.list\s+Return OVH Next Gen IP LoadBalancers services',
    ]

    for task_regex in tasks_regex:
        assert re.search(task_regex, output)
    assert error == ''
