from flask import Blueprint, request, Response
from google.oauth2 import id_token
from google.auth.transport import requests
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from src.config import GOOGLE_AUDIENCE
from src.enums import DemoSite
from src.models.user import User
import json


auth = Blueprint("auth", __name__)


@auth.route("/google-auth", methods=["POST"])
def google_auth():
    idToken = request.json["idToken"]
    try: id_info = id_token.verify_oauth2_token(idToken, requests.Request(), GOOGLE_AUDIENCE)
    except ValueError: return Response({'error': 'Invalid user'}, status=401)
    user = User.objects(googleId=id_info["sub"])
    
    if user:
        user.update(
            email=id_info["email"],
            firstName=id_info["given_name"],
            lastName=id_info["family_name"],
            name=id_info["name"],
            photoUrl=id_info["picture"],
            googleId=id_info["sub"],
        )
    else:
        User(
            email=id_info["email"],
            firstName=id_info["given_name"],
            lastName=id_info["family_name"],
            name=id_info["name"],
            photoUrl=id_info["picture"],
            googleId=id_info["sub"],
        ).save()
    
    user = User.get_user_by_email(id_info["email"]).to_mongo_dict()
    access_token = create_access_token(identity=id_info["email"])

    return Response(json.dumps({"accessToken": access_token, "user": user}), status=200)


@auth.route("/profile", methods=["PATCH"])
@jwt_required()
def update_profile():
    user = User.get_user_by_email(get_jwt_identity())
    data = request.json
    user.update(demoSite=data["demoSite"])
    user.reload()
    user = user.to_mongo_dict()
    
    return Response(json.dumps({"user": user, "msg": f"Your demo site is updated to: {user['demoSite']}"}), status=200)


# Endpoint to retrieve all users
@auth.route("/users", methods=["GET"])
@jwt_required()
def get_users():
    users = User.objects()
    users = [user.to_mongo_dict() for user in users]
    return Response(json.dumps(users), status=200)


@auth.route("/user", methods=["GET"])
@jwt_required()
def get_user():
    user = User.get_user_by_email(get_jwt_identity())
    return Response(json.dumps(user.to_mongo_dict()), status=200)