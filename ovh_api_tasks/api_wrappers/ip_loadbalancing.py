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


def get_ip_lb_service_http_farms(ovh_client, service, zone=None):
    """
    Get next gen load balancing service HTTP farms

    GET /ip/LoadBalancing/{serviceName}/http/farm
    """

    url = '/ipLoadbalancing/{service}/http/farm'

    if zone:
        return ovh_client.get(url.format(service=quote_plus(service)), zone=zone)

    return ovh_client.get(url.format(service=quote_plus(service)))


def get_ip_lb_service_http_farm(ovh_client, service, farm):
    """
    Get next gen load balancing service HTTP farm

    GET /ip/LoadBalancing/{serviceName}/http/farm/{farmId}
    """

    url = '/ipLoadbalancing/{service}/http/farm/{farm}'

    return ovh_client.get(url.format(service=quote_plus(service), farm=farm))


def add_ip_lb_service_http_farm(ovh_client, service, farm_data):
    """
    Add next gen load balancing service HTTP farm

    POST /ip/LoadBalancing/{serviceName}/http/farm
    """

    url = '/ipLoadbalancing/{service}/http/farm'

    return ovh_client.post(url.format(service=quote_plus(service)), **farm_data)


def del_ip_lb_service_http_farm(ovh_client, service, farm):
    """
    Remove next gen load balancing service HTTP farm

    DELETE /ip/LoadBalancing/{serviceName}/http/farm/{farmId}
    """

    url = '/ipLoadbalancing/{service}/http/farm/{farm}'

    return ovh_client.delete(url.format(service=quote_plus(service), farm=farm))


def get_ip_lb_service_http_farm_servers(ovh_client, service, farm):
    """
    Get next gen load balancing service HTTP farm servers

    GET /ip/LoadBalancing/{serviceName}/http/farm/{farmId}/server
    """

    url = '/ipLoadbalancing/{service}/http/farm/{farm}/server'

    return ovh_client.get(url.format(service=quote_plus(service), farm=farm))


def get_ip_lb_service_http_farm_server(ovh_client, service, farm, server):
    """
    Get next gen load balancing service HTTP farm server

    GET /ip/LoadBalancing/{serviceName}/http/farm/{farmId}/server/{serverId}
    """

    url = '/ipLoadbalancing/{service}/http/farm/{farm}/server/{server}'

    return ovh_client.get(url.format(service=quote_plus(service), farm=farm, server=server))


def add_ip_lb_service_http_farm_server(ovh_client, service, farm, server_data):
    """
    Add next gen load balancing service HTTP farm server

    POST /ip/LoadBalancing/{serviceName}/http/farm/{farmId}/server
    """

    url = '/ipLoadbalancing/{service}/http/farm/{farm}/server'

    return ovh_client.post(url.format(service=quote_plus(service), farm=farm), **server_data)


def update_ip_lb_service_http_farm_server(ovh_client, service, farm, server, server_data):
    """
    Update next gen load balancing service HTTP farm server

    PUT /ip/LoadBalancing/{serviceName}/http/farm/{farmId}/server/{serverId}
    """

    url = '/ipLoadbalancing/{service}/http/farm/{farm}/server/{server}'

    return ovh_client.put(
        url.format(service=quote_plus(service), farm=farm, server=server),
        **server_data)


def del_ip_lb_service_http_farm_server(ovh_client, service, farm, server):
    """
    Remove next gen load balancing service HTTP farm server

    DELETE /ip/LoadBalancing/{serviceName}/http/farm/{farmId}/server/{serverId}
    """

    url = '/ipLoadbalancing/{service}/http/farm/{farm}/server/{server}'

    return ovh_client.delete(url.format(service=quote_plus(service), farm=farm, server=server))


def get_ip_lb_service_http_frontends(ovh_client, service):
    """
    Get next gen load balancing service HTTP frontends

    GET /ip/LoadBalancing/{serviceName}/http/frontend
    """

    url = '/ipLoadbalancing/{service}/http/frontend'

    return ovh_client.get(url.format(service=quote_plus(service)))


def get_ip_lb_service_http_frontend(ovh_client, service, frontend):
    """
    Get next gen load balancing service HTTP frontend

    GET /ip/LoadBalancing/{serviceName}/http/frontend/{frontendId}
    """

    url = '/ipLoadbalancing/{service}/http/frontend/{frontend}'

    return ovh_client.get(url.format(service=quote_plus(service), frontend=frontend))


def add_ip_lb_service_http_frontend(ovh_client, service, frontend_data):
    """
    Add next gen load balancing service HTTP frontend

    POST /ip/LoadBalancing/{serviceName}/http/frontend
    """

    url = '/ipLoadbalancing/{service}/http/frontend'

    return ovh_client.post(url.format(service=quote_plus(service)), **frontend_data)


def del_ip_lb_service_http_frontend(ovh_client, service, frontend):
    """
    Remove next gen load balancing service HTTP frontend

    DELETE /ip/LoadBalancing/{serviceName}/http/frontend/{frontendId}
    """

    url = '/ipLoadbalancing/{service}/http/frontend/{frontend}'

    return ovh_client.delete(url.format(service=quote_plus(service), frontend=frontend))


def get_ip_lb_service_tcp_farms(ovh_client, service, zone=None):
    """
    Get next gen load balancing service HTTP farms

    GET /ip/LoadBalancing/{serviceName}/tcp/farm
    """

    url = '/ipLoadbalancing/{service}/tcp/farm'

    if zone:
        return ovh_client.get(url.format(service=quote_plus(service)), zone=zone)

    return ovh_client.get(url.format(service=quote_plus(service)))


def get_ip_lb_service_tcp_farm(ovh_client, service, farm):
    """
    Get next gen load balancing service HTTP farm

    GET /ip/LoadBalancing/{serviceName}/tcp/farm/{farmId}
    """

    url = '/ipLoadbalancing/{service}/tcp/farm/{farm}'

    return ovh_client.get(url.format(service=quote_plus(service), farm=farm))


def add_ip_lb_service_tcp_farm(ovh_client, service, farm_data):
    """
    Add next gen load balancing service HTTP farm

    POST /ip/LoadBalancing/{serviceName}/tcp/farm
    """

    url = '/ipLoadbalancing/{service}/tcp/farm'

    return ovh_client.post(url.format(service=quote_plus(service)), **farm_data)


def del_ip_lb_service_tcp_farm(ovh_client, service, farm):
    """
    Remove next gen load balancing service HTTP farm

    DELETE /ip/LoadBalancing/{serviceName}/tcp/farm/{farmId}
    """

    url = '/ipLoadbalancing/{service}/tcp/farm/{farm}'

    return ovh_client.delete(url.format(service=quote_plus(service), farm=farm))


def get_ip_lb_service_tcp_farm_servers(ovh_client, service, farm):
    """
    Get next gen load balancing service HTTP farm servers

    GET /ip/LoadBalancing/{serviceName}/tcp/farm/{farmId}/server
    """

    url = '/ipLoadbalancing/{service}/tcp/farm/{farm}/server'

    return ovh_client.get(url.format(service=quote_plus(service), farm=farm))


def get_ip_lb_service_tcp_farm_server(ovh_client, service, farm, server):
    """
    Get next gen load balancing service HTTP farm server

    GET /ip/LoadBalancing/{serviceName}/tcp/farm/{farmId}/server/{serverId}
    """

    url = '/ipLoadbalancing/{service}/tcp/farm/{farm}/server/{server}'

    return ovh_client.get(url.format(service=quote_plus(service), farm=farm, server=server))


def add_ip_lb_service_tcp_farm_server(ovh_client, service, farm, server_data):
    """
    Add next gen load balancing service HTTP farm server

    POST /ip/LoadBalancing/{serviceName}/tcp/farm/{farmId}/server
    """

    url = '/ipLoadbalancing/{service}/tcp/farm/{farm}/server'

    return ovh_client.post(url.format(service=quote_plus(service), farm=farm), **server_data)


def update_ip_lb_service_tcp_farm_server(ovh_client, service, farm, server, server_data):
    """
    Update next gen load balancing service HTTP farm server

    PUT /ip/LoadBalancing/{serviceName}/tcp/farm/{farmId}/server/{serverId}
    """

    url = '/ipLoadbalancing/{service}/tcp/farm/{farm}/server/{server}'

    return ovh_client.put(
        url.format(service=quote_plus(service), farm=farm, server=server),
        **server_data)


def del_ip_lb_service_tcp_farm_server(ovh_client, service, farm, server):
    """
    Remove next gen load balancing service HTTP farm server

    DELETE /ip/LoadBalancing/{serviceName}/tcp/farm/{farmId}/server/{serverId}
    """

    url = '/ipLoadbalancing/{service}/tcp/farm/{farm}/server/{server}'

    return ovh_client.delete(url.format(service=quote_plus(service), farm=farm, server=server))


def get_ip_lb_service_tcp_frontends(ovh_client, service):
    """
    Get next gen load balancing service HTTP frontends

    GET /ip/LoadBalancing/{serviceName}/tcp/frontend
    """

    url = '/ipLoadbalancing/{service}/tcp/frontend'

    return ovh_client.get(url.format(service=quote_plus(service)))


def get_ip_lb_service_tcp_frontend(ovh_client, service, frontend):
    """
    Get next gen load balancing service HTTP frontend

    GET /ip/LoadBalancing/{serviceName}/tcp/frontend/{frontendId}
    """

    url = '/ipLoadbalancing/{service}/tcp/frontend/{frontend}'

    return ovh_client.get(url.format(service=quote_plus(service), frontend=frontend))


def add_ip_lb_service_tcp_frontend(ovh_client, service, frontend_data):
    """
    Add next gen load balancing service HTTP frontend

    POST /ip/LoadBalancing/{serviceName}/tcp/frontend
    """

    url = '/ipLoadbalancing/{service}/tcp/frontend'

    return ovh_client.post(url.format(service=quote_plus(service)), **frontend_data)


def del_ip_lb_service_tcp_frontend(ovh_client, service, frontend):
    """
    Remove next gen load balancing service HTTP frontend

    DELETE /ip/LoadBalancing/{serviceName}/tcp/frontend/{frontendId}
    """

    url = '/ipLoadbalancing/{service}/tcp/frontend/{frontend}'

    return ovh_client.delete(url.format(service=quote_plus(service), frontend=frontend))


def refresh_ip_lb_service(ovh_client, service, zone=None):
    """
    Apply next gen load balancing service configuration

    POST /ip/LoadBalancing/{serviceName}/refresh
    """

    url = '/ipLoadbalancing/{service}/refresh'

    return ovh_client.post(url.format(service=quote_plus(service)), zone=zone)


def get_ip_lb_service_ssl_items(ovh_client, service):
    """
    Get next gen load balancing service SSL items

    GET /ip/LoadBalancing/{serviceName}/ssl
    """

    url = '/ipLoadbalancing/{service}/ssl'

    return ovh_client.get(url.format(service=quote_plus(service)))


def get_ip_lb_service_ssl_item(ovh_client, service, ssl_item_id):
    """
    Get next gen load balancing service SSL item

    GET /ip/LoadBalancing/{serviceName}/ssl/{id}
    """

    url = '/ipLoadbalancing/{service}/ssl/{ssl_item_id}'

    return ovh_client.get(
        url.format(service=quote_plus(service), ssl_item_id=ssl_item_id))


def add_ip_lb_service_ssl_item(ovh_client, service, ssl_item_data):
    """
    Add next gen load balancing service SSL item

    POST /ip/LoadBalancing/{serviceName}/ssl
    """

    url = '/ipLoadbalancing/{service}/ssl'

    return ovh_client.post(url.format(service=quote_plus(service)), **ssl_item_data)


def del_ip_lb_service_ssl_item(ovh_client, service, ssl_item_id):
    """
    Remove next gen load balancing service SSL item

    DELETE /ip/LoadBalancing/{serviceName}/ssl/{id}
    """

    url = '/ipLoadbalancing/{service}/ssl/{ssl_item_id}'

    return ovh_client.delete(url.format(service=quote_plus(service), ssl_item_id=ssl_item_id))
