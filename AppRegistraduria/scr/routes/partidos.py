from flask import jsonify, request, make_response
from controllers.partidos import PartidosController


partidos_controller = PartidosController()

# crear Partido
def insert_partido():
    body = request.get_json()
    try:
        partido = partidos_controller.get_by_id(body['id_partido'])
        if partido:
            return make_response({
                'message': 'El partido con identificación ' + body['id_partido'] + ' Ya está registrado en el sistema'
            }, 400)
        partidos_controller.create(body)
        return make_response({
            'message': 'El partido ' + body['name'] + ' Ha sido creado satisfactoriamente.'
        }, 201)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error en la creación del partido'
        }, 500)

# Buscar Partidos
def find_partidos():
    try:
        partidos = partidos_controller.get_all()
        return make_response(jsonify(partidos), 200)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información de los partidos'
        }, 500)

# Buscar partido
def find_partido(partido_id):
    try:
        partido = partidos_controller.get_by_id(partido_id)
        if partido:
            return make_response(jsonify(partido), 200)
        else:
            return make_response({
                'message': 'El partido con num. de identificación ' + partido_id + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información del partido'
        }, 500)

# Borrar partido
def delete_partido(partido_id):
    try:
        delete = partidos_controller.delete(partido_id)
        if delete:
            return make_response({
                'message': 'El partido con num. de identificación ' + partido_id + ' fue eliminado satisfactoriamente'
            }, 200)
        else:
            return make_response({
                'message': 'El partido con num. de identificación ' + partido_id + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al eliminar al partido'
        }, 500)

# Actualizar partido
def update_partido(partido_id):
    body = request.get_json()
    try:
        update = partidos_controller.update(partido_id, body)
        if update:
            return make_response({
                'message': 'El partido con identificación ' + partido_id + ' actualizado satisfactoriamente'
            }, 200)
        else:
            return make_response({
            'message': 'No hay partido político con núm. de identificación ' + partido_id
        }, 400)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al actualizar la información del partido'
        }, 500)