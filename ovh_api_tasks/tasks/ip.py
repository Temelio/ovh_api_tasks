"""
Tasks about IPs
"""

import ovh
from invoke import task
from tabulate import tabulate

from ovh_api_tasks.api_wrappers import ip as ip_api_wrapper


@task(name='ips', default=True)
def get_ips(context):  # pylint: disable=unused-argument
    """
    Return IPs
    """

    ips_details = []
    ips_expired = []
    ovh_client = ovh.Client()

    # Get list of IPs
    ips = ip_api_wrapper.get_ips(ovh_client)

    # Get details for each ips
    for current_ip in ips:

        try:
            ip_data = ip_api_wrapper.get_ip(ovh_client, current_ip)
            ips_details.append([
                ip_data['type'],
                ip_data['routedTo']['serviceName'],
                ip_data['ip']
            ])
        except ovh.exceptions.APIError as error:
            if 'this service is expired' in str(error).lower():
                ips_expired.append([current_ip])
            else:
                raise

    print(tabulate(ips_details, headers=['Type', 'Service name', 'IP blocks']))
    print('\n\n', tabulate(ips_expired, headers=['Expired IP blocks']))
