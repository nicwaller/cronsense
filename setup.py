from setuptools import setup, find_packages
import os

version_file = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'cronsense', 'VERSION'))
version = version_file.read().strip()

setup(
    name='cronsense',
    version=version,
    author='Nic Waller',
    author_email='code@nicwaller.com',
    description='A cron wrapper that tells you more about your cron jobs',
    url='https://github.com/nicwaller/cronsense',
    install_requires=[
        'PyYAML',
    ],
    entry_points={
        "console_scripts": [
            "cronsense=cronsense.main:main",
        ]
    },
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'cronsense': ['cronsense/VERSION'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
      ]
)
