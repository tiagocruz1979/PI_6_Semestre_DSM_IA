from flask import Flask
from flask import Blueprint

from .knn_route import bp as bp_knn

bp_api = Blueprint("api", __name__, url_prefix="/api")


def init_app(app: Flask):
    bp_api.register_blueprint(bp_knn)

    app.register_blueprint(bp_api)
