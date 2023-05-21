from flask import Blueprint, jsonify, request
from flask_restplus import Namespace, Resource
from models.UserModel import UserModel
from utils.Validations import Validations
from models.entities.User import User
main = Blueprint('user-blueprint', __name__)
namespace = Namespace(
    'user-namespace', description='User CRUD and average age functions')


@main.route('/')
def get_users():
    try:
        users = UserModel.get_users()
        return jsonify(users)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<user_id>')
def get_user(user_id):
    try:
        user = UserModel.get_user(user_id)
        if user != None:
            return jsonify(user)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/', methods=['POST'])
def create_user():
    try:
        cedula_identidad = request.json['cedula_identidad']
        nombre = request.json['nombre']
        primer_apellido = request.json['primer_apellido']
        segundo_apellido = request.json['segundo_apellido']
        fecha_nacimiento = request.json['fecha_nacimiento']
        if cedula_identidad != None and Validations.check_numbers(cedula_identidad) and nombre != None and primer_apellido != None and segundo_apellido != None and fecha_nacimiento != None and Validations.is_valid_date(fecha_nacimiento):
            user = User(cedula_identidad, nombre, primer_apellido,
                        segundo_apellido, fecha_nacimiento)
            affected_rows = UserModel.create_user(user)
            if affected_rows == 1:
                return jsonify(user.cedula_identidad)
            else:
                return jsonify({'message': 'Error on insert'}), 500
        else:
            return jsonify({}), 400
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        affected_rows = UserModel.delete_user(user_id)
        if affected_rows == 1:
            return jsonify(user_id)
        else:
            return jsonify({'message': 'No user deleted'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        nombre = request.json['nombre']
        primer_apellido = request.json['primer_apellido']
        segundo_apellido = request.json['segundo_apellido']
        fecha_nacimiento = request.json['fecha_nacimiento']
        if nombre != None and primer_apellido != None and segundo_apellido != None and fecha_nacimiento != None and Validations.is_valid_date(fecha_nacimiento):
            user = User(user_id, nombre, primer_apellido,
                        segundo_apellido, fecha_nacimiento)
            affected_rows = UserModel.update_user(user)
            if affected_rows == 1:
                return jsonify(user.cedula_identidad)
            else:
                return jsonify({'message': 'No user updated'}), 404
        else:
            return jsonify({}), 400
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/average-age')
def get_average_age():
    try:
        average_age = UserModel.get_average_age()
        return jsonify(average_age)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
