#!/usr/bin/env python

# https://packaging.python.org/distributing/#setup-py

try:
    from setuptools import setup, find_packages
except ImportError as e:
    raise RuntimeError("Unable to find setuptools; please visit https://pypi.python.org/pypi/setuptools for instructions", e)

import os.path

NAME = 'python-kms-trta'

package_includes = ['*']
package_excludes = ['build', 'dist', 'examples', 'tests', '*.egg-info']
packages = find_packages(include=package_includes, exclude=package_excludes)

requirements = [
    'boto3',
    ]

test_requirements = [
    # TODO: put package test requirements here
    ]

setup(
    # https://packaging.python.org/distributing/#setup-args
    name=NAME,
    version='0.1.0',
    description="Toolkit for creating encrypted keys.",
    long_description="Toolkit for creating encrypted keys.",
    author="Chad.Sandquist",
    author_email='chad.sandquist@thomsonreuters.com',
    maintainer='TRTA Cloud Scrum Team',
    maintainer_email='TRTACloudScrumTeam@thomsonreuters.com',
    url='https://git.sami.int.thomsonreuters.com/trta-cloud-scrum-team/tbd',
    packages=packages,
    include_package_data=True,
    install_requires=requirements,
    # Install this package as individual files, not a zipped egg
    zip_safe=False,
    keywords='amazon aws kms',
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Installation/Setup',
        'Topic :: Utilities',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
