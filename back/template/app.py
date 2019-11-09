import rq_dashboard
from flask import Flask
from flask_cors import CORS

from .api import register_api
from .auth import create_google_auth
from .config import flask_config
from .core.cache import REDIS_URL
from .storage import create_storage_gw


def create_app(api=True):
    app = Flask(__name__)
    CORS(app, resources={r"*": {"origins": "*"}}, supports_credentials=True)
    app.config.from_object(flask_config)

    create_google_auth(app)
    create_storage_gw(app)

    if api:
        register_api(app)

    app.config.from_object(rq_dashboard.default_settings)
    app.config['REDIS_URL'] = REDIS_URL
    app.register_blueprint(rq_dashboard.blueprint, url_prefix="/jobs")

    return app
