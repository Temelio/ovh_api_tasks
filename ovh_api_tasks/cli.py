"""
CLI management for OVH API actions
"""

from invoke import Collection, Program
from .tasks import ovh_api as ovh_api_tasks


def main(args=None):
    """
    Manage CLI entry point to work with OVH API
    """

    program = Program(
        name='Invoke taks over OVH API',
        namespace=Collection.from_module(ovh_api_tasks),
        version='0.1.0-alpha+001')

    program.run(args)
