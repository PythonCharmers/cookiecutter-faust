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
def parse_requirements(path):
    """
    Parse requirements files to allow easier separation in to groups.

    Keep the line filtering simple, but we could go the whole way in implementing
    https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format
    if required.
    """
    for line in open(path):
        line = line.strip()
        if not line or line.startswith('#'):
            continue

        if line.startswith('-r'): # looking at another requirements file
            yield from parse_requirements(line[2:].strip())
        else:
            yield line

install_requires = list(parse_requirements('requirements.txt'))
dev_install_requires = list(parse_requirements('dev-requirements.txt'))


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
