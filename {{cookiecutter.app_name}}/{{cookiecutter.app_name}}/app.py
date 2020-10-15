import faust


app = faust.App(
    '{{cookiecutter.app_name}}',
    broker='{{ cookiecutter.kafka_broker }}',
    store='{{ cookiecutter.kafka_store }}',
    version=1,
    autodiscover=True,
    origin='{{cookiecutter.app_name}}'   # imported name for this project (import proj -> "proj")
)


def main() -> None:
    app.main()
