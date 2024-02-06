from flask import Blueprint, request, Response
from src.models.indicators import Indicator

rcrft = Blueprint("rcrft", __name__)

@rcrft.route("/get-all-indicators", methods=["GET"])
def get_all_indicators():
    all_indicators = Indicator.objects().to_json()
    return Response(all_indicators, status=200)