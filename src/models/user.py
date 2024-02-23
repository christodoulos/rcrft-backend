from src.config import MONGO_DBNAME
from src.enums import DemoSite
import mongoengine as me


class User(me.Document):
    email = me.EmailField(required=True, unique=True)
    firstName = me.StringField(required=True)
    lastName = me.StringField(required=True)
    name = me.StringField(required=True)
    googleId = me.StringField(required=True)
    photoUrl = me.StringField(required=True)
    provider = me.StringField(required=True, choices=["GOOGLE"], default="GOOGLE")
    demoSite = me.EnumField(DemoSite, required=True, default=DemoSite.NONE)

    meta = {"collection": "users", "db_alias": MONGO_DBNAME}
    

    def to_mongo_dict(self):
        mongo_dict = self.to_mongo().to_dict()
        mongo_dict.pop("_id")
        return mongo_dict
    

    def get_user_by_google_id(googleId: str) -> "User":
        return User.objects(googleId=googleId).first()
    
    
    def get_user_by_email(email: str) -> "User":
        return User.objects(email=email).first()