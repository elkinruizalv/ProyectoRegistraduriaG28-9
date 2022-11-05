from controllers.abstract import CRUDController
from models.candidato import Candidato

class CandidatosController(CRUDController):
    def __init__(self) -> None:
        super().__init__()

    def get_all(self):
        candidatos = []
        for candidato in Candidato.objects:
            candidatos.append(candidato)
        return candidatos

    def get_by_id(self, id_item):
        return Candidato.objects(cedula=id_item).first()

    def create(self, content):
        candidato = Candidato(
            cedula=content['cedula'],
            nombre=content['nombre'],
            apellido=content['apellido'],
            resolucion=content['resolucion']            
        )
        candidato.save()
        return candidato
    
    def update(self, id_item, content):
        candidato = self.get_by_id(id_item)
        if candidato:
            candidato.update(
                nombre=content.get('nombre', candidato.nombre),
                apellido=content.get('apellido', candidato.apellido)                
            )
            return candidato
        return None
    
    def delete(self, id_item):
        candidato = self.get_by_id(id_item)
        if candidato:
            candidato.delete()
            return candidato
        return None

