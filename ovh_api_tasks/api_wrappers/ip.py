"""
Main level for OVH API calls
"""

from urllib.parse import quote_plus
from tenacity import retry
from tenacity.stop import stop_after_delay
from tenacity.wait import wait_fixed


def get_ips(ovh_client):
    """
    Get all ips informations

    GET /ip
    """

    return ovh_client.get('/ip')


def get_ip(ovh_client, ip_address):
    """
    Get all ips informations

    GET /ip/{ip}
    """

    return ovh_client.get('/ip/{ip}'.format(ip=quote_plus(ip_address)))


def get_ip_lb_services(ovh_client):
    """
    Get all legacy load balancing services

    GET /ip/LoadBalancing
    """

    return ovh_client.get('/ip/loadBalancing')


def get_ip_lb_service(ovh_client, service):
    """
    Get legacy load balancing service details

    GET /ip/LoadBalancing/{serviceName}
    """

    url = '/ip/loadBalancing/{service}'

    return ovh_client.get(url.format(service=quote_plus(service)))


def get_ip_lb_service_backends(ovh_client, service):
    """
    Get legacy load balancing service backends

    GET /ip/LoadBalancing/{serviceName}/backend
    """

    url = '/ip/loadBalancing/{service}/backend'

    return ovh_client.get(url.format(service=quote_plus(service)))


def get_ip_lb_service_backend(ovh_client, service, backend):
    """
    Get legacy load balancing service backend detail

    GET /ip/LoadBalancing/{serviceName}/backend/{backend}
    """

    url = '/ip/loadBalancing/{service}/backend/{backend}'

    return ovh_client.get(url.format(
        service=quote_plus(service), backend=backend))



def add_ip_lb_service_backend(ovh_client, service, backend, probe):
    """
    Add backend to legacy load balancing service

    POST /ip/loadBalancing/{serviceName}/backend
    ipBackend = {backend}
    probe = {probe}
    """

    url = '/ip/loadBalancing/{service}/backend'

    task_obj = ovh_client.post(
        url.format(service=quote_plus(service)),
        ipBackend=backend,
        probe=probe)

    print('INFO - Link "{backend}" to "{service}" : task {task_id}'.format(
        backend=backend, service=service, task_id=task_obj['id']))

    _waiting_ip_lb_service_tasks_done(ovh_client, service)


def delete_ip_lb_service_backend(ovh_client, service, backend):
    """
    Delete backend from legacy load balancing service

    DELETE /ip/loadBalancing/{serviceName}/backend/{backend}
    """

    url = '/ip/loadBalancing/{service}/backend/{backend}'

    task_obj = ovh_client.delete(url.format(
        service=quote_plus(service),
        backend=backend))

    print('INFO - Unlink "{backend}" from "{service}" : task {task_id}'.format(
        backend=backend, service=service, task_id=task_obj['id']))

    _waiting_ip_lb_service_tasks_done(ovh_client, service)


def get_ip_lb_service_tasks(ovh_client, service):
    """
    Get all tasks linked to a legacy load balancer

    GET /ip/loadBalancing/{serviceName}/task
    """

    url = '/ip/loadBalancing/{service}/task'

    return ovh_client.get(url.format(service=quote_plus(service)))


def get_ip_lb_service_task(ovh_client, service, task_id):
    """
    Get legacy load balancing tasks details

    GET /ip/loadBalancing/{serviceName}/task/{taskId}
    """

    url = '/ip/loadBalancing/{service}/task/{task_id}'

    return ovh_client.get(url.format(
        service=quote_plus(service),
        task_id=task_id))


@retry(stop=stop_after_delay(10), wait=wait_fixed(2))
def _waiting_ip_lb_service_tasks_done(ovh_client, service):  # pylint: disable=invalid-name
    """
    Waiting legacy load balancing has no tasks in progress
    """

    tasks = get_ip_lb_service_tasks(ovh_client, service)
    tasks_count = len(tasks)

    if tasks_count == 0:
        return True

    print('  {service} - {tasks_count} tasks in progress : {tasks}'.format(
        service=service, tasks_count=tasks_count, tasks=tasks))

    return False
