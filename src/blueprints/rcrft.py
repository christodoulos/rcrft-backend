from flask import Blueprint, Response, request
from src.models.indicators import Indicator, CodeAndDescription
from flask_jwt_extended import get_jwt_identity, jwt_required
import json

rcrft = Blueprint("rcrft", __name__)

@rcrft.route("/get-all-indicators", methods=["GET"])
@jwt_required()
def get_all_indicators():
    current_user = get_jwt_identity()
    print(current_user)
    all_indicators = Indicator.objects().to_json()
    return Response(all_indicators, status=200)


@rcrft.route("/get-category-names", methods=["GET"])
@jwt_required()
def get_category_names():
    current_user = get_jwt_identity()
    categoryNames = Indicator.objects().distinct("category.description")
    return Response(json.dumps({"categoryNames": categoryNames}), status=200)


@rcrft.route("/get-subcategory-names", methods=["GET"])
@jwt_required()
def get_subcategory_names():
    current_user = get_jwt_identity()
    subcategoryNames = Indicator.objects().distinct("subcategory.description")
    return Response(json.dumps({"subcategoryNames": subcategoryNames}), status=200)


@rcrft.route("add-indicator", methods=["POST"])
@jwt_required()
def add_indicator():
    current_user = get_jwt_identity()
    data = request.get_json()
    
    Indicator(
        **data
    ).save()
    
    return Response(json.dumps({"msg": "Indicator added"}), status=200)
