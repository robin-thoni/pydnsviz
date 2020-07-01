#! /usr/bin/env python3

from setuptools import setup, find_packages


setup(
    name='pydnsviz',
    version="0.1.0",

    description="CLI tool to visualize DNS zones",
    long_description="""\
CLI tool to visualize DNS record in a graph to show dependencies""",

    url='https://github.com/robin-thoni/pydnsviz',
    author="Robin Thoni",
    author_email='robin@rthoni.com',

    license='MIT',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: System Administrators',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords="dns graphviz dot",

    packages=find_packages(),
    install_requires=[
        'argparse',
        'graphviz',
        'dnspython',
    ],

    extras_require={
        'dev': [],
        'test': [],
    },

    package_data={
    },

    data_files=[
    ],

    entry_points={
        'console_scripts': [
            'pydnsviz=pydnsviz.main:entrypoint',
        ],
    },

    cmdclass={
    }
)
