from peewee import *

db = SqliteDatabase("products.db")


class Product(Model):
    name = CharField(unique=True)
    price = FloatField()
    category = CharField()

    class Meta:
        database = db


db.connect()
db.create_tables([Product])
