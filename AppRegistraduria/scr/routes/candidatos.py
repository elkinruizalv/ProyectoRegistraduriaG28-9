from flask import jsonify, request, make_response
from controllers.candidatos import CandidatosController

candidatos_controller = CandidatosController()

# crear Candidato
def insert_candidato():
    body = request.get_json()
    try:
        candidato = candidatos_controller.get_by_id(body['cedula'])
        if candidato:
            return make_response({
                'message': 'El candidato con cedula ' + body['cedula'] + ' Ya está registrado en el sistema'
            }, 400)
        candidatos_controller.create(body)
        return make_response({
            'message': 'El candidato con cedula' + body['cedula'] + ' Ha sido creado satisfactoriamente.'
        }, 201)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error en la creación del candidato'
        }, 500)

# Buscar Candidatos
def find_candidatos():
    try:
        candidatos = candidatos_controller.get_all()
        return make_response(jsonify(candidatos), 200)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información de los candidatos'
        }, 500)

# Buscar candidato
def find_candidato(candidato_id):
    try:
        candidato = candidatos_controller.get_by_id(candidato_id)
        if candidato:
            return make_response(jsonify(candidato), 200)
        else:
            return make_response({
                'message': 'El candidato identificado con número ' + candidato_id + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al obtener la información del candidato'
        }, 500)

# Borrar candidato
def delete_candidato(candidato_id):
    try:
        delete = candidatos_controller.delete(candidato_id)
        if delete:
            return make_response({
                'message': 'El candidato identificado con número ' + candidato_id + ' fue eliminado satisfactoriamente'
            }, 200)
        else:
            return make_response({
                'message': 'El candidato identificado con número ' + candidato_id + ' no fue encontrado'
            }, 404)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al eliminar al candidato'
        }, 500)

# Actualizar candidato
def update_candidato(candidato_id):
    body = request.get_json()
    try:
        update = candidatos_controller.update(candidato_id, body)
        if update:
            return make_response({
                'message': 'El candidato con identificación ' + candidato_id + ' actualizado satisfactoriamente'
            }, 200)
        else:
            return make_response({
            'message': 'No hay candidato con número de identificación ' + candidato_id
        }, 400)
    except Exception as ex:
        print(ex)
        return make_response({
            'message': 'Hubo un error al actualizar la información del candidato'
        }, 500)