from peewee import DoesNotExist, IntegrityError

from template.core import cache
from template.exceptions import *
from template.models.social.user import User


def get_all(search=None) -> list:
    users = []
    if search is None or search == '':
        query = User.select()
    else:
        query = User.select().where(
            (User.first_name.contains(search)) |
            (User.last_name.contains(search)))

    for user in query:
        users.append(user.get_data())
    logger.debug('Get all users from db. Number of users : {}'.format(len(users)))

    return users


def get(user_id) -> User:
    try:
        user = User.get(User.id == user_id)
        return user
    except DoesNotExist:
        raise UserNotExisting


def get_by_mail(mail) -> User:
    try:
        user = User.get(User.email == mail)
        return user
    except DoesNotExist:
        raise UserNotExisting


def add_user(email, team) -> dict:
    try:
        user = User.create(email=email, team=team)
        return user.get_identity()
    except IntegrityError:
        raise UserAlreadyRegistered


def delete_user(user_id) -> bool:
    try:
        user = User.get(User.id == user_id)
        user.delete_instance(recursive=True)
        cache.set('user_{}_valid'.format(user_id), 'false')
        return True
    except DoesNotExist:
        raise UserNotExisting
