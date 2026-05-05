from peewee import SqliteDatabase, Model, CharField, FloatField

db = SqliteDatabase('products.db')

class Product(Model):
    name = CharField()
    price = FloatField()

    class Meta:
        database = db

def init_db():
    db.connect()
    db.create_tables([Product])