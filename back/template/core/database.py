from peewee import PostgresqlDatabase

from .config import config

db = PostgresqlDatabase(
    'template',
    user=config['database'].get('user'),
    password=config['database'].get('password'),
    host=config['database'].get('host'),
    autorollback=True
)
