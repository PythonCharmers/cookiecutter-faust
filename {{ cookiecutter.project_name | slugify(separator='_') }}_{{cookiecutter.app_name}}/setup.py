from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = "{{cookiecutter.version}}"

here = path.abspath(path.dirname(__file__))

# long description
# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# dependencies
# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs]

with open(path.join(here, 'dev-requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

dev_install_requires = [x.strip() for x in all_reqs]


# the actual setup, all done through the setup() function
setup(
    name='{{cookiecutter.app_name}}',
    version=__version__,

    # list of dependencies created above (from requirements.txt)
    install_requires=install_requires,

    # descriptions (including from README.md for long_description)
    description='{{cookiecutter.project_short_description}}',
    long_description=long_description,
    long_description_content_type='text/markdown', # as README.md is markdown

    # define what permissions you give for others to use (ie, what licence)
    license='All rights reserved',

    # find all sub-packages in root folder except docs and tests folders
    packages=find_packages(exclude=['docs', 'tests*']),

    # include additional files in MANIFEST.in
    include_package_data=True,
    author='{{cookiecutter.full_name}}',

    entry_points={
        'console_scripts': [
            '{{cookiecutter.app_name}} = {{cookiecutter.app_name}}.app:main',
        ]
    },

    extras_require={
        'dev': dev_install_requires
    }
)
