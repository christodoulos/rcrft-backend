from flask import Flask

from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from mongoengine import connect

app = Flask(__name__)

connect(db="rcrft", alias="rcrft")

cors = CORS(
    app,
    resources={r"*": {"origins": ["http://localhost:4200"]}},
)

SWAGGER_URL = "/docs"
API_URL = "/static/swagger.json"
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "RCRFT Tool API"},
)
app.register_blueprint(swaggerui_blueprint)
