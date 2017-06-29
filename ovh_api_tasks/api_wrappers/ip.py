"""
Main level for OVH API calls
"""

from urllib.parse import quote_plus


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

    return ovh_client.post(
        url.format(service=quote_plus(service)),
        ipBackend=backend,
        probe=probe)


def delete_ip_lb_service_backend(ovh_client, service, backend):
    """
    Delete backend from legacy load balancing service

    DELETE /ip/loadBalancing/{serviceName}/backend/{backend}
    """

    url = '/ip/loadBalancing/{service}/backend/{backend}'

    return ovh_client.delete(url.format(
        service=quote_plus(service),
        backend=backend))


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
