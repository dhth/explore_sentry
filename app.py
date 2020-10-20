from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from dotenv import load_dotenv
import os

load_dotenv()

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0,
    environment="dev"
)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/route")
def some_route():
    return some_var


@app.route("/someroute")
def some_other_route():
    return blipblop

@app.route("/buggyroute")
def buggy_route():
    return something

@app.route("/cmon")
def cmon():
    return a_variable
