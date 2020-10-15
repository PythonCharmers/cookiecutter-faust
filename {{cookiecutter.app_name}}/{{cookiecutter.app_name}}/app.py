import faust

from . import __version__


app = faust.App(
    '{{cookiecutter.app_name}}',
    version=__version__,
    autodiscover=True,
    origin='{{cookiecutter.app_name}}'   # imported name for this project (import proj -> "proj")
)


def main() -> None:
    app.main()
