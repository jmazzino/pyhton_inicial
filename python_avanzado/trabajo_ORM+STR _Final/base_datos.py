from peewee import *
import datetime

try:
    db = SqliteDatabase("agenda_piwi.db")

    class BaseModel(Model):
        class Meta:
            database = db

    class Agenda(BaseModel):
        id = AutoField(unique=True)
        nombre = CharField()
        apellido = CharField()
        interno = SmallIntegerField()
        email = CharField()

        def __str__(
            self,
        ):
            return "Este es el interno: " + self.apellido

    db.connect()
    db.create_tables([Agenda])

except:
    print("mmmm")
