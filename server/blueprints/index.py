from flask import Blueprint, jsonify
from ..services.health_service import get_basic_health

index = Blueprint('index', __name__)


@index.route("/")
def hello_world():
    health = {"internal": get_basic_health(1)}
    return jsonify(health)

@index.route("/level/<level>")
def byebye_world(level):
    health = {"internal": get_basic_health(int(level))}
    return jsonify(health)