import mongoengine as me

class Partido(me.Document):
    id_partido= me.IntField(required=True)
    name = me.StringField(required=True)
    lema = me.StringField(required=True)

    def to_json(self, *args, **kwargs):
        return super().to_json(*args, **kwargs)