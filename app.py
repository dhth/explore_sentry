from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
import os

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0,
)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/debug-sentry")
def trigger_error():
    division_by_zero = 1 / 0
