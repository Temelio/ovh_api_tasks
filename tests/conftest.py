"""
Tests configuration and fixtures import
"""

# pylint: disable=unused-import

from tests.fixtures.exceptions import service_expired
from tests.fixtures.ip import ip_block_array, ip_v4, ip_v6
from tests.fixtures.load_balancing.legacy import \
    ip_lb_task_add_backend, \
    ip_lb_task_del_backend, \
    ip_load_balancing_array, \
    ip_load_balancing_ip
