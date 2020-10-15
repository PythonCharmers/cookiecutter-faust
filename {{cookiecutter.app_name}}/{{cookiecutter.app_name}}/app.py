import faust


app = faust.App(
    '{{cookiecutter.app_name}}',
    version=1,
    autodiscover=True,
    origin='{{cookiecutter.app_name}}'   # imported name for this project (import proj -> "proj")
)


def main() -> None:
    app.main()
