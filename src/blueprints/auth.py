from flask import Blueprint, request, Response
from google.oauth2 import id_token
from google.auth.transport import requests
from flask_jwt_extended import create_access_token
from src.config import GOOGLE_AUDIENCE
from src.models.user import User
import json


auth = Blueprint("auth", __name__)


@auth.route("/google-auth", methods=["POST"])
def google_auth():
    idToken = request.json["idToken"]
    try: id_info = id_token.verify_oauth2_token(idToken, requests.Request(), GOOGLE_AUDIENCE)
    except ValueError: return Response({'error': 'Invalid user'}, status=401)
    
    User.objects(googleId=id_info["sub"]).update_one(
        email=id_info["email"],
        firstName=id_info["given_name"],
        lastName=id_info["family_name"],
        name=id_info["name"],
        photoUrl=id_info["picture"],
        googleId=id_info["sub"],
        upsert=True,
    )
    
    access_token = create_access_token(identity=id_info["email"])

    return Response(json.dumps({"accessToken": access_token}), status=200)
