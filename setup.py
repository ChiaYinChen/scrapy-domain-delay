"""Package this project."""
from setuptools import find_packages, setup

import scrapy_domain_delay


setup(
    name='scrapy-domain-delay',
    version=scrapy_domain_delay.__version__,
    description='Define download_delay for different domain.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    author='Carol Chen',
    author_email='carolchency@gmail.com',
    classifiers=[
        'Framework :: Scrapy',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.7',
    install_requires=[
        'scrapy>=1.6.0',
        'tldextract==2.2.1',
    ],
)
