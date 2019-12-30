from peewee import *

from template.core import db
from template.models.social.user import User


class FBCredentials(Model):
    id = PrimaryKeyField()
    user = ForeignKeyField(User, unique=True)
    token = CharField()
    fb_user_id = CharField()
    expires_in = IntegerField()
    signed_request = TextField()
    data_access_expiration_time = IntegerField()

    class Meta:
        database = db


with db:
    FBCredentials.create_table(fail_silently=True)
