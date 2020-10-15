# CookieCutter Faust project

A cookiecutter template for python faust projects intended to be pip-installed

[cookiecutter](https://github.com/audreyr/cookiecutter)

Forked from: [PythonCharmers/cookiecutter-pipproject](https://github.com/PythonCharmers/cookiecutter-pipproject.git)


## Using CookieCutter for your project

    $ pip install cookiecutter
    $ cookiecutter gh:PythonCharmers/cookiecutter-faust

You will be asked about your basic info (name, project name, app name, etc.). This info will be used in your new project.

## Running your faust project

First install the project via pip with:

```bash
pip install -e .
```

Then the project is runnable from the command line with:

```bash
proj worker -l info
```

or as a module with:

```bash
python -m proj worker -l info
```

## Publishing your project to pypi

Follow the instructions [here](https://packaging.python.org/tutorials/packaging-projects/) and use twine to publish to the Python Package Index.
 

## Goals

The goal of this project is simply to take some of the boiler plate out of creating a new Faust project. It is based on
the recommendations from [the Faust documentation](https://faust.readthedocs.io/en/latest/userguide/application.html#medium-large-projects).
It includes:

- Sphinx documentation
- Installable via pip in pypi
- Runnable from the command line via the application name
- Testing via pytest, hypothesis and coverage

In the future, we may include some other things like:

- basic travic ci configuration
- anything else you think might make sense (open up an issue with ideas).


## Contributing

The intent of this project is to stay fairly lean, but if you have any suggestions or would like to help out, please let me know.


## License

BSD licensed.
