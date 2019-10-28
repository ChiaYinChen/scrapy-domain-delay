"""Python Setup file."""
from setuptools import setup, find_packages

import scrapy_domain_delay

setup(
    name='scrapy-domain-delay',
    version=scrapy_domain_delay.__version__,
    description='Define download_delay for different domain.',
    packages=find_packages(),
    install_requires=[
        'Scrapy>=1.6.0',
        'tldextract==2.2.1',
    ],
    author='Carol Chen',
    author_email='carolchency@gmail.com'
)
