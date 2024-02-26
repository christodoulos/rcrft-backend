from flask import Blueprint, Response, request
from src.models.indicators import *
from src.models.user import *
from src.interfaces import *
from typing import List
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


@rcrft.route("/new-assessment", methods=["POST"])
@jwt_required()
def new_assessment():
	current_user = get_jwt_identity()
	data = request.get_json()

	indicator = Indicator.get_by_description(data["description"])
	form_type = data["formType"]

	if not indicator: return Response(json.dumps({"msg": "Indicator not found"}), status=404)

	if form_type == "qualitative":
		new_assessment = Assessment(
			user=current_user,
			normalized_value=data["normalizedValue"],
		)

	elif form_type == "quantitative-reference":
		new_assessment = Assessment(
			user=current_user,
			value=data["value"],
			reference_value=data["referenceValue"],
			is_inverse=data["isInverse"],
			alternative_description=data["alternativeDescription"],
			normalized_value=data["normalizedValue"],
		)

	elif form_type == "quantitative-min-max":
		new_assessment = Assessment(
			user=current_user,
			value=data["value"],
			min_value=data["minValue"],
			max_value=data["maxValue"],
   			is_inverse=data["isInverse"],
			alternative_description=data["alternativeDescription"],
			normalized_value=data["normalizedValue"],
		)
  
	else: return Response(json.dumps({"msg": "Form type not found"}), status=404)

	indicator.assessments.append(new_assessment)
	indicator.save()
	return Response(json.dumps({"msg": "Assessment added"}), status=200)



@rcrft.route("/get-all-assessments", methods=["GET"])
@jwt_required()
def get_all_assessments():
	current_user = get_jwt_identity()

	all_indicators = Indicator.objects()
	final_assessments: List[IAssessment] = []
 
	for indicator in all_indicators:
		for assessment in indicator.assessments:
			new_assessment: IAssessment = {
				"indicator": indicator.description,
				"user": assessment.user,
				"value": assessment.value,
				"reference_value": assessment.reference_value,
				"min_value": assessment.min_value,
				"max_value": assessment.max_value,
				"is_inverse": assessment.is_inverse,
				"alternative_description": assessment.alternative_description,
				"normalized_value": assessment.normalized_value,
    			"demoSite": User.get_user_by_email(assessment.user).demoSite.value
			}
			final_assessments.append(new_assessment)
	print(final_assessments)
	return Response(json.dumps(final_assessments), status=200)
