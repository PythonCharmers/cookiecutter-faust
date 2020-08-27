CookieCutter Pip-Project
========================

A cookiecutter template for python projects intended to be pip-installed

[cookiecutter](https://github.com/audreyr/cookiecutter)

Forked from: [sloria](https://github.com/wdm0006/cookiecutter-pipproject.git)


Using CookieCutter for your project
-----------------------------------

    $ pip install cookiecutter
    $ cookiecutter gh:PythonCharmers/cookiecutter-pipproject

You will be asked about your basic info (name, project name, app name, etc.). This info will be used in your new project.


Publishing your project to pypi
-------------------------------

Follow the instructions [here](https://packaging.python.org/tutorials/packaging-projects/) and use twine to publish to the Python Package Index.
 
Goals
-----

The goal of this project is simply to take some of the boiler plate out of creating a new python project. It is intended
to stay pretty minimal, but contains everything needed to make a project that includes:

 * Sphinx documentation
 * Installable via pip in pypi
 * Testing via pytest, hypothesis and coverage

In the future, we may include some other things like:

 * basic travic ci configuration
 * anything else you think might make sense (open up an issue with ideas).
 
Contributing
------------

The intent of this project is to stay fairly lean, but if you have any suggestions or would like to help out, please let me know.

License
-------

BSD licensed.
