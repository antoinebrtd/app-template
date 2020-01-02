from peewee import PostgresqlDatabase

from .config import config

db = PostgresqlDatabase(
    'flask_app',
    user=config['database'].get('user'),
    password=config['database'].get('password'),
    host=config['database'].get('host'),
    autorollback=True
)
