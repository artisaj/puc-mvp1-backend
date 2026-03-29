from flask import Flask
from flasgger import Swagger
from flask_cors import CORS

from .database.connection import init_db
from .routes.pilotos_routes import pilotos_bp
from .routes.corridas_routes import corridas_bp


def create_app():
    app = Flask(__name__)
    app.config["SWAGGER"] = {
        "title": "API Kart MVP",
        "uiversion": 3,
    }

    CORS(app)
    Swagger(app)

    init_db()

    app.register_blueprint(pilotos_bp, url_prefix="/api")
    app.register_blueprint(corridas_bp, url_prefix="/api")

    @app.get("/")
    def healthcheck():
        return {"status": "ok", "service": "kart-api"}, 200

    return app
