from controllers.abstract import CRUDController
from models.partido import Partido

class PartidosController(CRUDController):
    def __init__(self) -> None:
        super().__init__()

    def get_all(self):
        partidos = []
        for partido in Partido.objects:
            partidos.append(partido)
        return partidos

    def get_by_id(self, id_item):
        return Partido.objects(id_partido=id_item).first()

    def create(self, content):
        partido = Partido(
            id_partido=content['id_partido'],
            name=content['name'],
            lema=content['lema']
        )
        partido.save()
        return partido
    
    def update(self, id_item, content):
        partido = self.get_by_id(id_item)
        if partido:
            partido.update(
                name=content.get('name', partido.name), 
                lema=content.get('lema', partido.lema)
            )
            return partido
        return None
    
    def delete(self, id_item):
        partido = self.get_by_id(id_item)
        if partido:
            partido.delete()
            return partido
        return None

