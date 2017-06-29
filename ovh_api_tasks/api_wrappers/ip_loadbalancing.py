"""
Main level for OVH API calls usin /ipLoadbalancing root url
"""

from urllib.parse import quote_plus


def get_ip_lb_available_zones(ovh_client):
    """
    Get all next gen load balancing available zones

    GET /ipLoadbalancing/availableZones
    """

    return ovh_client.get('/ipLoadbalancing/availableZones')


def get_ip_lb_services(ovh_client):
    """
    Get all next gen load balancing services

    GET /ipLoadbalancing
    """

    return ovh_client.get('/ipLoadbalancing')


def get_ip_lb_service(ovh_client, service):
    """
    Get next gen load balancing service details

    GET /ipLoadbalancing/{serviceName}
    """

    url = '/ipLoadbalancing/{service}'

    return ovh_client.get(url.format(service=quote_plus(service)))


def get_ip_lb_service_farms(ovh_client, service):
    """
    Get next gen load balancing service farms

    GET /ipLoadbalancing/{serviceName}/definedFarms
    """

    url = '/ipLoadbalancing/{service}/definedFarms'

    return ovh_client.get(url.format(service=quote_plus(service)))


def get_ip_lb_service_fo_ip(ovh_client, service):
    """
    Get next gen load balancing service failover IPs

    GET /ipLoadbalancing/{serviceName}/failover
    """

    url = '/ipLoadbalancing/{service}/failover'

    return ovh_client.get(url.format(service=quote_plus(service)))


def get_ip_lb_service_frontends(ovh_client, service):
    """
    Get next gen load balancing service frontends

    GET /ipLoadbalancing/{serviceName}/definedFrontends
    """

    url = '/ipLoadbalancing/{service}/definedFrontends'

    return ovh_client.get(url.format(service=quote_plus(service)))


def get_ip_lb_service_routes(ovh_client, service):
    """
    Get next gen load balancing service routes

    GET /ipLoadbalancing/{serviceName}/definedRoutes
    """

    url = '/ipLoadbalancing/{service}/definedRoutes'

    return ovh_client.get(url.format(service=quote_plus(service)))


def get_ip_lb_service_instances_state(ovh_client, service):  # pylint: disable=invalid-name
    """
    Get next gen load balancing service instances state

    GET /ipLoadbalancing/{serviceName}/instancesState
    """

    url = '/ipLoadbalancing/{service}/instancesState'

    return ovh_client.get(url.format(service=quote_plus(service)))


def get_ip_lb_service_nat_ip_subnet(ovh_client, service):
    """
    Get next gen load balancing service NAT IP subnet

    GET /ipLoadbalancing/{serviceName}/natIp
    """

    url = '/ipLoadbalancing/{service}/natIp'

    return ovh_client.get(url.format(service=quote_plus(service)))


def get_ip_lb_service_infos(ovh_client, service):
    """
    Get next gen load balancing service additional informations

    GET /ip/LoadBalancing/{serviceName}/serviceInfos
    """

    url = '/ipLoadbalancing/{service}/serviceInfos'

    return ovh_client.get(url.format(service=quote_plus(service)))


def get_ip_lb_service_tasks(ovh_client, service):
    """
    Get next gen load balancing service tasks

    GET /ip/LoadBalancing/{serviceName}/task
    """

    url = '/ipLoadbalancing/{service}/task'

    return ovh_client.get(url.format(service=quote_plus(service)))


def get_ip_lb_service_task(ovh_client, service, task_id):
    """
    Get next gen load balancing service task

    GET /ip/LoadBalancing/{serviceName}/task/{id}
    """

    url = '/ipLoadbalancing/{service}/task/{id}'

    return ovh_client.get(url.format(service=quote_plus(service), id=task_id))
