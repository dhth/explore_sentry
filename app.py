from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from dotenv import load_dotenv
import os
from sentry_sdk import add_breadcrumb
from do_something import something, something_else, something_else_2
from sentry_sdk import set_user

load_dotenv()

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0,
    environment=os.getenv("APP_ENV"),
    release=os.getenv("SENTRY_RELEASE"),
)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/test3")
def test3():
    set_user({"email": "someuser@email.com"})
    var1 = something_else()
    return "Bye"


@app.route("/test4")
def test4():
    set_user({"email": "someuser@email.com"})
    var1 = something_else_2()
    return "Bye"
