import json

from peewee import *

from flask_app.core import db


class User(Model):
    id = PrimaryKeyField()
    first_name = CharField()
    last_name = CharField()
    email = CharField(unique=True, index=True)
    password = CharField(null=True)
    picture = TextField(null=True)
    last_login = DateTimeField()
    account_activated = BooleanField(default=False)
    first_login = BooleanField(default=False)
    created_at = DateTimeField()

    def get_identity(self):
        return {"id": self.id, "first_name": self.first_name, "last_name": self.last_name, "picture": self.picture,
                "email": self.email}

    def get_data(self):
        identity = self.get_identity()
        identity['name'] = "{} {}".format(self.first_name, self.last_name)
        return identity, self.account_activated, self.first_login

    def add_google_credentials(self, credentials):
        from flask_app.models.social.gcredentials import GCredentials
        data = credentials.copy()
        data['user'] = self.id
        data['scopes'] = json.dumps(data['scopes'])
        try:
            with db.atomic():
                GCredentials.create(**data)
        except IntegrityError:
            with db.transaction():
                GCredentials.delete().where(GCredentials.user == self.id).execute()
                GCredentials.create(**data)

    def get_google_credentials(self):
        from flask_app.models.social.gcredentials import GCredentials
        gcredentials = list(GCredentials.select().where(GCredentials.user == self.id).dicts())
        data = gcredentials[0].copy()
        data['scopes'] = json.loads(data['scopes'])
        del data['user']
        del data['id']
        return data

    def add_facebook_credentials(self, credentials):
        from flask_app.models.social.fbcredentials import FBCredentials
        data = credentials.copy()
        data['user'] = self.id
        data['scopes'] = json.dumps(data['scopes'])
        try:
            with db.atomic():
                FBCredentials.create(**data)
        except IntegrityError:
            with db.transaction():
                FBCredentials.delete().where(FBCredentials.user == self.id).execute()
                FBCredentials.create(**data)

    def get_facebook_credentials(self):
        from flask_app.models.social.fbcredentials import FBCredentials
        fbcredentials = list(FBCredentials.select().where(FBCredentials.user == self.id).dicts())
        data = fbcredentials[0].copy()
        data['scopes'] = json.loads(data['scopes'])
        del data['user']
        del data['id']
        return data

    class Meta:
        database = db


with db:
    User.create_table(fail_silently=True)
