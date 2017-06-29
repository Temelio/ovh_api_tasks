"""
Tasks about legacy Load Balancing
"""

from invoke import task
from invoke.exceptions import ParseError
import ovh
from tabulate import tabulate

from ovh_api_tasks.api_wrappers import ip as ip_api_wrapper
from ovh_api_tasks.utils import ip_lb as ip_lb_utils


def _build_list_task_line(service_data, service_backends):
    """
    Create a legacy Load Balancer line for list task
    """

    return [
        service_data['serviceName'],
        ', '.join(service_data['zone']).upper(),
        service_data['ipLoadBalancing'],
        ', '.join(service_backends),
        service_data['state'],
    ]


@task(name='list')
def get_legacy_lb(context):  # pylint: disable=unused-argument
    """
    Return OVH IP LoadBalancers services
    """

    services_details = []
    services_expired = []

    ovh_client = ovh.Client()

    # Get list of legacy LB IPs
    services = ip_api_wrapper.get_ip_lb_services(ovh_client)

    # Get details for each ips
    for service in services:
        try:
            service_data = ip_api_wrapper.get_ip_lb_service(
                ovh_client, service)
            service_backends = ip_api_wrapper.get_ip_lb_service_backends(
                ovh_client, service)

            services_details.append(
                _build_list_task_line(service_data, service_backends))
        except ovh.exceptions.APIError as error:
            if 'this service is expired' not in str(error).lower():
                raise
            services_expired.append([service])

    print(tabulate(services_details, headers=[
        'Service name', 'Zone', 'Load Balancing IP', 'Backends', 'State']))
    print('\n\n', tabulate(services_expired, headers=['Expired services']))


@task(name='add-backend')
def add_backend_to_legacy_lb(context, backend, services, probe):  # pylint: disable=unused-argument
    """
    Add a backend to legacy IP LoadBalancer services
    """

    ovh_client = ovh.Client()
    ip_lb_services = ip_api_wrapper.get_ip_lb_services(ovh_client)

    for service in services.split(','):

        if service not in ip_lb_services:
            raise ParseError('{} is not a valid service'.format(service))

        service_backends = ip_api_wrapper.get_ip_lb_service_backends(
            ovh_client, service)

        if backend in service_backends:
            print('INFO - Backend {backend} already linked to {service}'.format(
                backend=backend, service=service))
            continue

        try:
            ovh_task = ip_api_wrapper.add_ip_lb_service_backend(
                ovh_client, service, backend, probe)

            print('INFO - Link "{backend}" to "{service}" : task {task}'.format(
                backend=backend, service=service, task=ovh_task['id']))

            ip_lb_utils.waiting_ip_lb_service_tasks_done(ovh_client, service, 'legacy')
        except ovh.exceptions.APIError as error:
            output = ('ERROR - Add {backend} to {service} : {error}')
            print(output.format(backend=backend, service=service, error=error))


@task(name='del-backend')
def remove_backend_from_legacy_lb(context, backend, services):  # pylint: disable=unused-argument
    """
    Remove a backend from legacy IP LoadBalancer services
    """

    ovh_client = ovh.Client()
    ip_lb_services = ip_api_wrapper.get_ip_lb_services(ovh_client)

    for service in services.split(','):

        if service not in ip_lb_services:
            raise ParseError('{} is not a valid service'.format(service))

        service_backends = ip_api_wrapper.get_ip_lb_service_backends(
            ovh_client, service)

        if backend not in service_backends:
            print('INFO - Backend {backend} not linked to {service}'.format(
                backend=backend, service=service))
            continue

        try:
            ovh_task = ip_api_wrapper.delete_ip_lb_service_backend(
                ovh_client, service, backend)

            print('INFO - Unlink "{backend}" from "{service}" : task {task}'.format(
                backend=backend, service=service, task=ovh_task['id']))

            ip_lb_utils.waiting_ip_lb_service_tasks_done(ovh_client, service, 'legacy')
        except ovh.exceptions.APIError as error:
            output = ('ERROR - Remove {backend} from {service} : {error}')
            print(output.format(backend=backend, service=service, error=error))
