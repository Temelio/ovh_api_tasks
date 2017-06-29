"""
Utils function for IP LBs
"""

from ovh_api_tasks.api_wrappers import ip_loadbalancing as ip_lb_next_gen
from ovh_api_tasks.api_wrappers import ip as ip_lb_legacy
from tenacity import retry, TryAgain
from tenacity.stop import stop_after_delay
from tenacity.wait import wait_fixed


@retry(stop=stop_after_delay(10), wait=wait_fixed(2))
def waiting_ip_lb_service_tasks_done(ovh_client, service, lb_type):  # pylint: disable=invalid-name
    """
    Waiting load balancing service has no tasks in progress
    """

    if lb_type == 'legacy':
        tasks = ip_lb_legacy.get_ip_lb_service_tasks(ovh_client, service)
    elif lb_type == 'next_gen':
        tasks = ip_lb_next_gen.get_ip_lb_service_tasks(ovh_client, service)

    tasks_count = len(tasks)

    if tasks_count == 0:
        print('  {service} - All tasks done'.format(service=service))
        return True

    print('  {service} - {tasks_count} task(s) in progress : {tasks}'.format(
        service=service, tasks_count=tasks_count, tasks=tasks))

    raise TryAgain
