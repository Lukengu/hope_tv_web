import os

from flask import Flask
from src.shared.routes import Route


def create_app():
    app = Flask(__name__)
    Route.init_route(app)
    return app
