"""
Tasks about next generation (HAproxy) Load Balancing
"""

import yaml
from invoke import task
from invoke.exceptions import ParseError
import ovh
from tabulate import tabulate

from ovh_api_tasks.api_wrappers import ip_loadbalancing as ip_lb_api_wrapper


def _build_service_list_display_line(service_data, service_farms):
    """
    Create a next gen Load Balancer line for service display
    """

    return [
        service_data['serviceName'],
        ', '.join(service_data['zone']).upper(),
        service_data['ipLoadbalancing'],
        service_data['ipv6'],
        ', '.join('{}({})'.format(farm['type'], farm['id']) for farm in service_farms),
        service_data['sslConfiguration'],
        service_data['displayName'],
        service_data['state'],
        service_data['offer'],
    ]


def _display_services_data(active_services, expired_services):
    """
    Manage next gen Load Balancer HTTP farms display
    """

    print(tabulate(active_services, headers=[
        'Service name',
        'Zone',
        'Load Balancing IP',
        'IPv6',
        'Farms',
        'SSL configuration',
        'Display name',
        'State',
        'Offer',
    ]))
    print('\n\n', tabulate(expired_services, headers=['Expired services']))


def _build_http_or_tcp_farm_display_line(service, farm_data):
    """
    Create a next gen Load Balancer line for HTTP farm
    """

    return [
        service,
        farm_data['displayName'],
        farm_data['farmId'],
        farm_data['balance'],
        farm_data['zone'].upper(),
        farm_data['port'],
        farm_data['probe'],
        farm_data['stickiness'],
    ]


def _display_http_or_tcp_farms_data(farms):
    """
    Manage next gen Load Balancer HTTP farms display
    """

    print(tabulate(farms, headers=[
        'Service name',
        'Display name',
        'Farm ID',
        'Balance',
        'Zone',
        'Port',
        'Probe',
        'Stickiness',
    ]))


def _build_http_or_tcp_server_display_line(service, server_data):
    """
    Create a next gen Load Balancer line for HTTP server display
    """

    return [
        service,
        server_data['backendId'],
        server_data['serverId'],
        server_data['displayName'],
        server_data['address'],
        server_data['port'],
        server_data['status'],
        server_data['weight'],
        server_data['ssl'],
        server_data.get('cookie', 'N/A'),
        server_data['proxyProtocolVersion'],
        server_data['chain'],
        server_data['backup'],
        server_data['probe'],
    ]


def _display_http_or_tcp_servers_data(servers):
    """
    Manage next gen Load Balancer HTTP farm servers display
    """

    print(tabulate(servers, headers=[
        'Service name',
        'Farm ID',
        'Server ID',
        'Display name',
        'Address',
        'Port',
        'Status',
        'Weight',
        'SSL',
        'Cookie',
        'Proxy protocol version',
        'Chain',
        'Backup',
        'Probe',
    ]))


def _build_http_or_tcp_frontend_display_line(service, frontend_data):
    """
    Create a next gen Load Balancer line for HTTP frontend display
    """

    return [
        service,
        frontend_data['frontendId'],
        frontend_data['displayName'],
        frontend_data['zone'],
        frontend_data['port'],
        frontend_data['defaultFarmId'],
        frontend_data['ssl'],
        frontend_data['defaultSslId'],
        frontend_data['dedicatedIpfo'],
        frontend_data['hsts'],
        frontend_data['allowedSource'],
        frontend_data['httpHeader'],
        frontend_data['redirectLocation'],
    ]


def _display_http_or_tcp_frontends_data(servers):
    """
    Manage next gen Load Balancer HTTP farm servers display
    """

    print(tabulate(servers, headers=[
        'Service name',
        'Frontend ID',
        'Display name',
        'Zone',
        'Port',
        'Default Farm ID',
        'SSL',
        'Default SSL ID',
        'Dedicated IP FO',
        'HSTS',
        'Allowed source',
        'HTTP header',
        'Redirect location',
    ]))


def _build_ssl_item_display_line(service, ssl_item_data):
    """
    Create a next gen Load Balancer line for SSL item display
    """

    return [
        service,
        ssl_item_data['id'],
        ssl_item_data['displayName'],
        ssl_item_data['subject'],
        ssl_item_data['fingerprint'],
        ssl_item_data['type'],
    ]


def _display_ssl_items_data(ssl_items):
    """
    Manage next gen Load Balancer SSL items display
    """

    print(tabulate(ssl_items, headers=[
        'Service name',
        'SSL item ID',
        'Display name',
        'Subject',
        'Fingerprint',
        'Type',
    ]))


def _get_next_gen_lb_http_or_tcp_farms(service, farm_type):
    """
    Return OVH Next Gen IP LoadBalancers service HTTP or TCP farms
    """

    farms_details = []
    ovh_client = ovh.Client()

    if farm_type == 'http':
        _get_farms = ip_lb_api_wrapper.get_ip_lb_service_http_farms
        _get_farm = ip_lb_api_wrapper.get_ip_lb_service_http_farm
    else:
        _get_farms = ip_lb_api_wrapper.get_ip_lb_service_tcp_farms
        _get_farm = ip_lb_api_wrapper.get_ip_lb_service_tcp_farm

    # Get list of next gen LB IP farms
    farms = _get_farms(ovh_client, service)

    # Get details for each farm
    for farm in farms:
        farm_data = _get_farm(ovh_client, service, farm)

        farms_details.append(
            _build_http_or_tcp_farm_display_line(service, farm_data))

    _display_http_or_tcp_farms_data(farms_details)


def _add_http_or_tcp_farm(service, zone, balance, display_name, port, stickiness, probe, farm_type):  # pylint: disable=unused-argument
    """
    Add an HTTP or TCP farm to next gen IP LoadBalancer service

    Probe must be defined using dict str.
    """

    ovh_client = ovh.Client()
    probe_data = None

    if farm_type == 'http':
        _add_farm = ip_lb_api_wrapper.add_ip_lb_service_http_farm
    else:
        _add_farm = ip_lb_api_wrapper.add_ip_lb_service_tcp_farm

    if probe:
        probe_data = yaml.load(probe)

    farm_data = {
        'balance': balance,
        'displayName': display_name,
        'port': port,
        'stickiness': stickiness,
        'zone': zone,
        'probe': probe_data
    }

    response = _add_farm(ovh_client, service, farm_data)

    _display_http_or_tcp_farms_data(_build_http_or_tcp_farm_display_line(service, response))


def _add_http_or_tcp_farm_server(service, farm, address, status, backup, chain, cookie, display_name, port, probe, proxy_protocol_version, ssl, weight, farm_type):  # pylint: disable=unused-argument
    """
    Add an HTTP or TCP farm server to next gen IP LoadBalancer service
    """

    ovh_client = ovh.Client()

    service_data = ip_lb_api_wrapper.get_ip_lb_service(ovh_client, service)

    server_data = {
        'address': address,
        'backup': backup,
        'chain': chain,
        'displayName': display_name,
        'port': port,
        'probe': probe,
        'proxyProtocolVersion': proxy_protocol_version,
        'ssl': ssl,
        'status': status,
        'weight': weight
    }

    if service_data.get('offer') == 'legacy':
        for unmanaged_key in ['chain', 'ssl']:
            server_data.pop(unmanaged_key)

    if farm_type == 'http':
        server_data['cookie'] = cookie
        _add_farm_server = ip_lb_api_wrapper.add_ip_lb_service_http_farm_server
    else:
        _add_farm_server = ip_lb_api_wrapper.add_ip_lb_service_tcp_farm_server

    response = _add_farm_server(ovh_client, service, farm, server_data)

    _display_http_or_tcp_servers_data([
        _build_http_or_tcp_server_display_line(service, response)])


def _get_next_gen_lb_http_or_tcp_farm_servers(service, farm, farm_type):
    """
    Return OVH Next Gen IP LoadBalancers service HTTP or TCP farm servers
    """

    servers_details = []
    ovh_client = ovh.Client()

    if farm_type == 'http':
        _get_servers = ip_lb_api_wrapper.get_ip_lb_service_http_farm_servers
        _get_server = ip_lb_api_wrapper.get_ip_lb_service_http_farm_server
    else:
        _get_servers = ip_lb_api_wrapper.get_ip_lb_service_tcp_farm_servers
        _get_server = ip_lb_api_wrapper.get_ip_lb_service_tcp_farm_server

    # Get list of next gen LB IP farms
    servers = _get_servers(ovh_client, service, farm)

    # Get details for each server
    for server in servers:
        server_data = _get_server(ovh_client, service, farm, server)

        servers_details.append(
            _build_http_or_tcp_server_display_line(service, server_data))

    _display_http_or_tcp_servers_data(servers_details)


def _get_next_gen_lb_http_or_tcp_farm_frontends(service, frontend_type):
    """
    Return OVH Next Gen IP LoadBalancers service HTTP or TCP frontends
    """

    frontends_details = []
    ovh_client = ovh.Client()

    if frontend_type == 'http':
        _get_frontends = ip_lb_api_wrapper.get_ip_lb_service_http_frontends
        _get_frontend = ip_lb_api_wrapper.get_ip_lb_service_http_frontend
    else:
        _get_frontends = ip_lb_api_wrapper.get_ip_lb_service_tcp_frontends
        _get_frontend = ip_lb_api_wrapper.get_ip_lb_service_tcp_frontend

    # Get list of next gen LB IP farms
    frontends = _get_frontends(ovh_client, service)

    # Get details for each server
    for frontend in frontends:
        frontend_data = _get_frontend(ovh_client, service, frontend)

        frontends_details.append(
            _build_http_or_tcp_frontend_display_line(service, frontend_data))

    _display_http_or_tcp_frontends_data(frontends_details)


def _add_http_or_tcp_frontend(service, zone, port, allowed_source, dedicated_ip_fo, default_farm_id, default_ssl_id, display_name, disabled, hsts, http_header, ssl, redirect_location, frontend_type):  # pylint: disable=unused-argument
    """
    Add an HTTP or TCP frontend to next gen IP LoadBalancer service
    """

    ovh_client = ovh.Client()
    allowed_source_data = []
    dedicated_ip_fo_data = []
    http_header_data = []

    if allowed_source:
        allowed_source_data = allowed_source.split(',')

    if dedicated_ip_fo:
        dedicated_ip_fo_data = dedicated_ip_fo.split(',')

    if http_header:
        http_header_data = http_header.split(',')

    frontend_data = {
        'allowedSource': allowed_source_data,
        'dedicatedIpfo': dedicated_ip_fo_data,
        'defaultFarmId': default_farm_id,
        'defaultSslId': default_ssl_id,
        'disabled': disabled,
        'displayName': display_name,
        'port': port,
        'redirectLocation': redirect_location,
        'ssl': ssl,
        'zone': zone
    }

    if frontend_type == 'http':
        frontend_data['hsts'] = hsts
        frontend_data['httpHeader'] = http_header_data,
        _add_frontend = ip_lb_api_wrapper.add_ip_lb_service_http_frontend
    else:
        _add_frontend = ip_lb_api_wrapper.add_ip_lb_service_tcp_frontend


    response = _add_frontend(ovh_client, service, frontend_data)

    _display_http_or_tcp_frontends_data([
        _build_http_or_tcp_frontend_display_line(service, response)])


@task(name='list')
def get_next_gen_lb(context):  # pylint: disable=unused-argument
    """
    Return OVH Next Gen IP LoadBalancers services
    """

    active_services = []
    expired_services = []

    ovh_client = ovh.Client()

    # Get list of next gen LB IPs
    services = ip_lb_api_wrapper.get_ip_lb_services(ovh_client)

    # Get details for each ips
    for service in services:
        try:
            service_data = ip_lb_api_wrapper.get_ip_lb_service(
                ovh_client, service)
            service_farms = ip_lb_api_wrapper.get_ip_lb_service_farms(
                ovh_client, service)

            active_services.append(
                _build_service_list_display_line(service_data, service_farms))
        except ovh.exceptions.APIError as error:
            if 'this service is expired' not in str(error).lower():
                raise
            expired_services.append([service])

    _display_services_data(active_services, expired_services)


@task(name='http-farms')
def get_next_gen_lb_http_farm(context, service):  # pylint: disable=unused-argument
    """
    Return OVH Next Gen IP LoadBalancers service HTTP farms
    """

    _get_next_gen_lb_http_or_tcp_farms(service, 'http')


@task(name='tcp-farms')
def get_next_gen_lb_tcp_farm(context, service):  # pylint: disable=unused-argument
    """
    Return OVH Next Gen IP LoadBalancers service HTTP farms
    """

    _get_next_gen_lb_http_or_tcp_farms(service, 'tcp')


@task(name='add-http-farm')
def add_http_farm(context, service, zone, balance=None, display_name='', port=None, stickiness=None, probe=None):  # pylint: disable=unused-argument
    """
    Add an HTTP farm to next gen IP LoadBalancer service

    Probe must be defined using dict str.
    """

    _add_http_or_tcp_farm(service, zone, balance, display_name, port, stickiness, probe, 'http')


@task(name='add-tcp-farm')
def add_tcp_farm(context, service, zone, balance=None, display_name='', port=None, stickiness=None, probe=None):  # pylint: disable=unused-argument
    """
    Add an TCP farm to next gen IP LoadBalancer service

    Probe must be defined using dict str.
    """

    _add_http_or_tcp_farm(service, zone, balance, display_name, port, stickiness, probe, 'tcp')


@task(name='del-http-farm')
def del_next_gen_lb_http_farm(context, service, farm):  # pylint: disable=unused-argument
    """
    Remove OVH Next Gen IP LoadBalancers service HTTP farm
    """

    ovh_client = ovh.Client()

    ip_lb_api_wrapper.del_ip_lb_service_http_farm(
        ovh_client, service, farm)

    print('HTTP farm "{farm}" removed successfully from "{service}".'.format(
        service=service, farm=farm))


@task(name='del-tcp-farm')
def del_next_gen_lb_tcp_farm(context, service, farm):  # pylint: disable=unused-argument
    """
    Remove OVH Next Gen IP LoadBalancers service TCP farm
    """

    ovh_client = ovh.Client()

    ip_lb_api_wrapper.del_ip_lb_service_tcp_farm(
        ovh_client, service, farm)

    print('TCP farm "{farm}" removed successfully from "{service}".'.format(
        service=service, farm=farm))


@task(name='add-http-server')
def add_http_farm_server(context, service, farm, address, status, backup=False, chain='', cookie=None, display_name='', port=None, probe=False, proxy_protocol_version=None, ssl=False, weight=None):  # pylint: disable=unused-argument
    """
    Add an HTTP farm server to next gen IP LoadBalancer service
    """

    _add_http_or_tcp_farm_server(service, farm, address, status, backup, chain, cookie, display_name, port, probe, proxy_protocol_version, ssl, weight, 'http')  # pylint: disable=unused-argument


@task(name='add-tcp-server')
def add_tcp_farm_server(context, service, farm, address, status, backup=False, chain='', cookie=None, display_name='', port=None, probe=False, proxy_protocol_version=None, ssl=False, weight=None):  # pylint: disable=unused-argument
    """
    Add a TCP farm server to next gen IP LoadBalancer service
    """

    _add_http_or_tcp_farm_server(service, farm, address, status, backup, chain, cookie, display_name, port, probe, proxy_protocol_version, ssl, weight, 'tcp')  # pylint: disable=unused-argument


@task(name='http-servers')
def get_next_gen_lb_http_farm_servers(context, service, farm):  # pylint: disable=unused-argument
    """
    Return OVH Next Gen IP LoadBalancers service HTTP farm servers
    """

    _get_next_gen_lb_http_or_tcp_farm_servers(service, farm, 'http')


@task(name='tcp-servers')
def get_next_gen_lb_tcp_farm_servers(context, service, farm):  # pylint: disable=unused-argument
    """
    Return OVH Next Gen IP LoadBalancers service TCP farm servers
    """

    _get_next_gen_lb_http_or_tcp_farm_servers(service, farm, 'tcp')


@task(name='del-http-server')
def del_next_gen_lb_http_farm_server(context, service, farm, server):  # pylint: disable=unused-argument
    """
    Remove OVH Next Gen IP LoadBalancers service HTTP farm server
    """

    ovh_client = ovh.Client()

    ip_lb_api_wrapper.del_ip_lb_service_http_farm_server(
        ovh_client, service, farm, server)

    print('{service} - Server "{server} removed successfully from HTTP farm "{farm}".'.format(
        service=service, farm=farm, server=server))


@task(name='del-tcp-server')
def del_next_gen_lb_tcp_farm_server(context, service, farm, server):  # pylint: disable=unused-argument
    """
    Remove OVH Next Gen IP LoadBalancers service TCP farm server
    """

    ovh_client = ovh.Client()

    ip_lb_api_wrapper.del_ip_lb_service_tcp_farm_server(
        ovh_client, service, farm, server)

    print('{service} - Server "{server} removed successfully from TCP farm "{farm}".'.format(
        service=service, farm=farm, server=server))


@task(name='http-frontends')
def get_next_gen_lb_http_frontends(context, service):  # pylint: disable=unused-argument
    """
    Return OVH Next Gen IP LoadBalancers service HTTP frontends
    """

    _get_next_gen_lb_http_or_tcp_farm_frontends(service, 'http')


@task(name='tcp-frontends')
def get_next_gen_lb_tcp_frontends(context, service):  # pylint: disable=unused-argument
    """
    Return OVH Next Gen IP LoadBalancers service HTTP frontends
    """

    _get_next_gen_lb_http_or_tcp_farm_frontends(service, 'tcp')


@task(name='add-http-frontend')
def add_http_frontend(context, service, zone, port, allowed_source=None, dedicated_ip_fo=None, default_farm_id=None, default_ssl_id=None, display_name='', disabled=False, hsts=False, http_header=None, ssl=False, redirect_location=''):  # pylint: disable=unused-argument
    """
    Add an HTTP frontend to next gen IP LoadBalancer service
    """

    _add_http_or_tcp_frontend(service, zone, port, allowed_source, dedicated_ip_fo, default_farm_id, default_ssl_id, display_name, disabled, hsts, http_header, ssl, redirect_location, 'http')  # pylint: disable=unused-argument


@task(name='add-tcp-frontend')
def add_tcp_frontend(context, service, zone, port, allowed_source=None, dedicated_ip_fo=None, default_farm_id=None, default_ssl_id=None, display_name='', disabled=False, hsts=False, http_header=None, ssl=False, redirect_location=''):  # pylint: disable=unused-argument
    """
    Add a TCP frontend to next gen IP LoadBalancer service
    """

    _add_http_or_tcp_frontend(service, zone, port, allowed_source, dedicated_ip_fo, default_farm_id, default_ssl_id, display_name, disabled, hsts, http_header, ssl, redirect_location, 'tcp')  # pylint: disable=unused-argument


@task(name='del-http-frontend')
def del_next_gen_lb_http_frontend(context, service, frontend):  # pylint: disable=unused-argument
    """
    Remove OVH Next Gen IP LoadBalancers service HTTP frontend
    """

    ovh_client = ovh.Client()

    ip_lb_api_wrapper.del_ip_lb_service_http_frontend(
        ovh_client, service, frontend)

    print('{service} - HTTP frontend "{frontend} removed successfully.'.format(
        service=service, frontend=frontend))


@task(name='del-tcp-frontend')
def del_next_gen_lb_tcp_frontend(context, service, frontend):  # pylint: disable=unused-argument
    """
    Remove OVH Next Gen IP LoadBalancers service TCP frontend
    """

    ovh_client = ovh.Client()

    ip_lb_api_wrapper.del_ip_lb_service_tcp_frontend(
        ovh_client, service, frontend)

    print('{service} - TCP frontend "{frontend} removed successfully.'.format(
        service=service, frontend=frontend))


@task(name='ssl-items')
def get_next_gen_lb_ssl_items(context, service):  # pylint: disable=unused-argument
    """
    Return OVH Next Gen IP LoadBalancers service SSL items
    """

    ssl_items_details = []

    ovh_client = ovh.Client()

    # Get list of next gen LB IP farms
    ssl_items = ip_lb_api_wrapper.get_ip_lb_service_ssl_items(ovh_client, service)

    # Get details for each server
    for ssl_item in ssl_items:
        ssl_item_data = ip_lb_api_wrapper.get_ip_lb_service_ssl_item(
            ovh_client, service, ssl_item)

        ssl_items_details.append(
            _build_ssl_item_display_line(service, ssl_item_data))

    _display_ssl_items_data(ssl_items_details)


@task(name='add-ssl-item')
def add_ssl_item(context, service, certificate, key, chain='', display_name=''):  # pylint: disable=unused-argument
    """
    Add an SSL item to next gen IP LoadBalancer service
    """

    ovh_client = ovh.Client()

    ssl_item_data = {
        'certificate': certificate,
        'key': key,
        'chain': chain,
        'displayName': display_name
    }

    response = ip_lb_api_wrapper.add_ip_lb_service_ssl_item(
        ovh_client, service, ssl_item_data)

    _display_ssl_items_data([
        _build_ssl_item_display_line(service, response)])


@task(name='del-ssl-item')
def del_next_gen_lb_ssl_item(context, service, ssl_item):  # pylint: disable=unused-argument
    """
    Remove OVH Next Gen IP LoadBalancers service SSL item
    """

    ovh_client = ovh.Client()

    ip_lb_api_wrapper.del_ip_lb_service_ssl_item(
        ovh_client, service, ssl_item)

    print('{service} - SSL item "{ssl_item} removed successfully.'.format(
        service=service, ssl_item=ssl_item))


@task(name='refresh')
def refresh_next_gen_lb_service(context, service):  # pylint: disable=unused-argument
    """
    Apply new configuration to OVH Next Gen IP LoadBalancers service
    """

    ovh_client = ovh.Client()

    ip_lb_api_wrapper.refresh_ip_lb_service(ovh_client, service)

    print('{service} - Configuration updated successfully.'.format(
        service=service))
