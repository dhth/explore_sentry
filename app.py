from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from dotenv import load_dotenv
import os
from sentry_sdk import add_breadcrumb

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


@app.route("/test1")
def test1():
    add_breadcrumb(
        category="auth",
        message="Authenticated user ",
        level="info",
    )
    return hellohello
