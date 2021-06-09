#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup file used to install package
"""

from setuptools import setup


def get_file_content(filename):
    """
    Return REAME.rst content
    """

    with open(filename) as file_handler:
        content = file_handler.read()

    return content


REQUIREMENTS = [
    'invoke==0.19.0',
    'ovh==0.4.7',
    'tabulate==0.7.7',
    'tenacity==4.2.0',
]

REQUIREMENTS_DEV = [
    'pip==19.2',
    'bumpversion==0.5.3',
    'wheel==0.29.0',
    'watchdog==0.8.3',
    'flake8==3.3.0',
    'tox==2.7.0',
    'coverage==4.4.1',
    'Sphinx==1.6.2',
    'cryptography==1.9',
    'PyYAML==3.12',
    'pytest==3.1.1',
    'pytest-cov==2.5.1',
    'pytest-mock==1.6.0',
    'pytest-pylint==0.7.1',
    'requests-mock==1.3.0',
    'spec==1.4.0',
]

setup(
    name='ovh_api_tasks',
    version='0.1.0+alpha001',
    description="Invoke tasks to work with OVH API",
    long_description=get_file_content('README.rst') + '\n\n' + get_file_content('HISTORY.rst'),
    author="Alexandre Chaussier",
    author_email='alexandre.chaussier@temelio.com',
    url='https://github.com/Temelio/ovh_api_tasks',
    packages=[
        'ovh_api_tasks',
        'ovh_api_tasks.api_wrappers',
        'ovh_api_tasks.tasks',
        'ovh_api_tasks.tasks.load_balancing',
    ],
    package_dir={'ovh_api_tasks':
                 'ovh_api_tasks'},
    entry_points={
        'console_scripts': [
            'ovh-api=ovh_api_tasks.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=REQUIREMENTS,
    license="MIT license",
    zip_safe=False,
    keywords='ovh_api_tasks',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=REQUIREMENTS_DEV
)
