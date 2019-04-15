#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import logging
import os
import subprocess
import sys


try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command

EGGNAME = 'pyrpo'
CONFIG = {
    'debug': True,
    'logname': '%s.setup.py' % EGGNAME,
    'logformat': '%(asctime)s %(name)s %(levelname)-5s %(message)s',
    'loglevel': logging.DEBUG,  # logging.INFO
}

logging.basicConfig(format=CONFIG['logformat'])
log = logging.getLogger(CONFIG['logname'])
log.setLevel(CONFIG['loglevel'])

SETUPPY_PATH = os.path.dirname(os.path.abspath(__file__))
# log.debug('SETUPPY_PATH: %s' % SETUPPY_PATH)


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


class PyTestCommand(Command):
    user_options = []
    description = "<TODO>"

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        cmd = ['pytest', '-v']

        globstr = os.path.join(SETUPPY_PATH, 'tests/test_*.py')
        cmd.extend(glob.glob(globstr))

        cmdstr = ' '.join(cmd)
        print(cmdstr)
        log.info(cmdstr)

        errno = subprocess.call(cmd)
        raise SystemExit(errno)


def build_long_description():
    with open('README.rst') as f:
        readme = f.read()
    with open('HISTORY.rst') as f:
        history = f.read().replace('. :changelog:', '')
    with open('AUTHORS.rst') as f:
        authors = f.read()
    return readme + '\n\n' + history + '\n\n' + authors


install_requires = [
    'python-dateutil',
]


setup(
    name='pyrpo',
    version='0.2.2',
    description=(
        'A shell command wrapper for hg, git, bzr, svn'),
    long_description=build_long_description(),
    author='Wes Turner',
    author_email='wes@wrd.nu',
    url='https://github.com/westurner/pyrpo',
    # download_url='https://github.com/westurner/pyrpo/releases',
    packages=[
        'pyrpo',
    ],
    package_dir={'pyrpo':
                 'pyrpo'},
    include_package_data=True,
    install_requires=install_requires,
    license="BSD",
    zip_safe=False,
    keywords='pyrpo hg git bzr svn',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'console_scripts': [
            'pyrpo=pyrpo.pyrpo:main'
        ]
    },
    test_suite='tests',
    cmdclass={
        'test': PyTestCommand,
    }
)
