#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'selenium==2.53.3'
]

test_requirements = [
    'Flask==0.12',
    'Flask-Testing==0.6.1'
]

setup(
    name='selenium_astride',
    version='0.2.1',
    description="Framework to use Selenium loud and clear, astride. Use it with Django, Flask or your favourite web framework.",
    long_description=readme + '\n\n' + history,
    author="Juan Madurga",
    author_email='jlmadurga@gmail.com',
    url='https://github.com/jlmadurga/python_selenium_astride',
    packages=[
        'selenium_astride',
    ],
    package_dir={'selenium_astride':
                 'selenium_astride'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='selenium_astride',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
