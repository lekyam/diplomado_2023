from flask import Blueprint, jsonify, request
from flask_restx import Namespace, Resource, fields
from models.UserModel import UserModel
from utils.Validations import Validations
from models.entities.User import User
main = Blueprint('user-blueprint', __name__)

user_namespace = Namespace(
    'users', description='User CRUD and average age functions')

user_post_expected_payload = user_namespace.model('User', {
    'cedula_identidad': fields.String(required=True, description='User Bolivia identification number '),
    'nombre': fields.String(required=True, description='User first name'),
    'primer_apellido': fields.String(required=True, description='User last name'),
    'segundo_apellido': fields.String(required=True, description='User second last name'),
    'fecha_nacimiento': fields.String(required=True, description='User birth date')
})


user_put_expected_payload = user_namespace.model('UserPut', {
    'nombre': fields.String(required=True, description='User first name'),
    'primer_apellido': fields.String(required=True, description='User last name'),
    'segundo_apellido': fields.String(required=True, description='User second last name'),
    'fecha_nacimiento': fields.String(required=True, description='User birth date')
})


@user_namespace.route('/')
class UsersResource(Resource):
    @user_namespace.doc('get_users', description='Retrieve the list of users.')
    def get(self):
        """Retrieve the list of users."""
        try:
            users = UserModel.get_users()
            return jsonify(users)
        except Exception as ex:
            return jsonify({'message': str(ex)}), 500

    @user_namespace.doc('create_user', description='Create a new user using the payload data.')
    @user_namespace.expect(user_post_expected_payload, validate=True)
    def post(self):
        """Create a new user"""
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


@user_namespace.route('<user_id>')
class UserResource(Resource):
    @user_namespace.doc('get-user-id', description='Get a user by their identification number.')
    def get(self, user_id):
        """Get a user by their ID"""
        try:
            user = UserModel.get_user(user_id)
            if user != None:
                return jsonify(user)
            else:
                return jsonify({}), 404
        except Exception as ex:
            return jsonify({'message': str(ex)}), 500

    @user_namespace.doc('delete-user', description='Delete a user by their identification number.')
    def delete(self, user_id):
        """Delete a user by their ID"""
        try:
            affected_rows = UserModel.delete_user(user_id)
            if affected_rows == 1:
                return jsonify(user_id)
            else:
                return jsonify({'message': 'No user deleted'}), 404
        except Exception as ex:
            return jsonify({'message': str(ex)}), 500

    @user_namespace.doc("update-user", description='Update a user by their identification number with the data provided in the payload.')
    @user_namespace.expect(user_put_expected_payload, validate=True)
    def put(self, user_id):
        """Update a user by their ID"""
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


@user_namespace.route('/average-age')
class AverageAgeResouce(Resource):
    @user_namespace.doc('get_average_age', description='Get the average age of the users.')
    def get(self):
        """Get the average age of users"""
        try:
            average_age = UserModel.get_average_age()
            return jsonify(average_age)
        except Exception as ex:
            return jsonify({'message': str(ex)}), 500
