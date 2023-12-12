from flask import Blueprint

from app.controllers import knn_controller

bp = Blueprint("knn", __name__, url_prefix="/knn")

bp.post("/analise")(knn_controller.analise)
