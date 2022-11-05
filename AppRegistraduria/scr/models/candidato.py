import mongoengine as me

class Candidato(me.Document):
    cedula= me.StringField(required=True)
    nombre = me.StringField(required=True)
    apellido = me.StringField(required=True)
    resolucion = me.StringField(required=True)

    def to_json(self, *args, **kwargs):
        return super().to_json(*args, **kwargs)