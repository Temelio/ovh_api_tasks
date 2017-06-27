=============
OVH API tasks
=============


.. image:: https://img.shields.io/pypi/v/ovh_api_tasks.svg
        :target: https://pypi.python.org/pypi/ovh_api_tasks

.. image:: https://img.shields.io/travis/Temelio/ovh_api_tasks.svg
        :target: https://travis-ci.org/Temelio/ovh_api_tasks

.. image:: https://readthedocs.org/projects/ovh-api-tasks/badge/?version=latest
        :target: https://ovh-api-tasks.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/Temelio/ovh_api_tasks/shield.svg
     :target: https://pyup.io/repos/github/Temelio/ovh_api_tasks/
     :alt: Updates


Invoke tasks to work with OVH API


* Free software: MIT license
* Documentation: https://ovh-api-tasks.readthedocs.io.

Testing
-------

To run tests locally, just run needed environments using tox:

``$ TOXENV=py27-ansible23 tox``

You can enable Paramiko debug if you have an error on Docker fixture create
(ex: ``Exception: Timeout reached while waiting on service!``)

``$ PARAMIKO_DEBUG=1 TOXENV=py27-ansible23 tox``

Commands
--------

Get IPs
~~~~~~~

    ``ovh-api ip.ips``

Return ips linked to the OVH account.

Add backend to legacy IP LB
~~~~~~~~~~~~~~~~~~~~~~~~~~~

    ``ovh-api lb.legacy.add-backend --backend=10.0.0.1 --services=ip-10.0.0.2,ip-10.0.0.3 --probe=http``

Add a backend to legacy IP LoadBalancer services.

Remove backend from legacy IP LB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    ``ovh-api lb.legacy.del-backend --backend=10.0.0.1 --services=ip-10.0.0.2,ip-10.0.0.3``

Remove a backend from legacy IP LoadBalancer services.

Get all legacy IP LB
~~~~~~~~~~~~~~~~~~~~

    ``ovh-api lb.legacy.list``

Return OVH IP LoadBalancers services.

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

