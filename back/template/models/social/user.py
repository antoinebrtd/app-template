import json

from peewee import *

from template.core import db


class User(Model):
    id = PrimaryKeyField()
    first_name = CharField(null=True)
    last_name = CharField(null=True)
    email = CharField(unique=True, index=True)
    picture = TextField(null=True)
    last_login = DateTimeField(null=True)

    def get_identity(self):
        return {"id": self.id, "first_name": self.first_name, "last_name": self.last_name, "picture": self.picture,
                "email": self.email}

    def get_data(self):
        identity = self.get_identity()
        if self.first_name is not None:
            identity['name'] = "{} {}".format(self.first_name, self.last_name)
        return identity

    def add_credentials(self, credentials):
        from template.models.social.gcredentials import GCredentials
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

    def get_credentials(self):
        from template.models.social.gcredentials import GCredentials
        gcredentials = list(GCredentials.select().where(GCredentials.user == self.id).dicts())
        data = gcredentials[0].copy()
        data['scopes'] = json.loads(data['scopes'])
        del data['user']
        del data['id']
        return data

    class Meta:
        database = db


with db:
    User.create_table(fail_silently=True)
