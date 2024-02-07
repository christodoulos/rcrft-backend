from flask import Blueprint, Response
from src.models.indicators import Indicator
from flask_jwt_extended import get_jwt_identity, jwt_required

rcrft = Blueprint("rcrft", __name__)

@rcrft.route("/get-all-indicators", methods=["GET"])
@jwt_required()
def get_all_indicators():
    current_user = get_jwt_identity()
    print(current_user)
    all_indicators = Indicator.objects().to_json()
    return Response(all_indicators, status=200)
