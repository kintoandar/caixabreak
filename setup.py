#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'lxml>=3.6.0',
    'requests>=2.10.0',
    'tabulate>=0.7.5'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='caixabreak',
    version='0.2.2',
    description="Extracts data from CGD - Caixa Break management interface",
    long_description=readme + '\n\n' + history,
    author="Joel Bastos",
    author_email='kintoandar@gmail.com',
    url='https://github.com/kintoandar/caixabreak',
    packages=[
        'caixabreak',
    ],
    package_dir={'caixabreak':
                 'caixabreak'},
    entry_points={
        'console_scripts': [
            'caixabreak=caixabreak.caixabreak:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='caixabreak',
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
    tests_require=test_requirements
)
