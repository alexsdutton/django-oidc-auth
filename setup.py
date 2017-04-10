# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='django-oidc-auth',
    version='0.0.11',
    description='OpenID Connect client for Django applications',
    long_description='WIP',
    author='Lucas S. Magalhães',
    author_email='lucas.sampaio@intelie.com.br',
    packages=find_packages(exclude=['*.tests']),
    include_package_data=True,
    install_requires=[
        'Django>=1.5',
        'pyjwkest>1.3.2,<1.4',
        'requests',
    ],
    zip_safe=True
)
