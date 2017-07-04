"""
Main level for OVH API calls
"""

from invoke import Collection
from ovh_api_tasks.tasks import ip as ip_tasks
from ovh_api_tasks.tasks.load_balancing import legacy as legacy_lb_tasks
from ovh_api_tasks.tasks.load_balancing import next_gen as next_gen_lb_tasks


# Invoke force name to namespace or ns
# pylint: disable=invalid-name

namespace = Collection()
namespace.add_collection(Collection.from_module(ip_tasks))
lb_collection = Collection('lb')
lb_collection.add_collection(Collection.from_module(legacy_lb_tasks))
lb_collection.add_collection(Collection.from_module(next_gen_lb_tasks))
namespace.add_collection(lb_collection)
