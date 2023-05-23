from flask import Blueprint, jsonify
from src.models.StatusModel import StatusModel
from flask_restx import Namespace, Resource
main = Blueprint('status-blueprint', __name__)
status_namespace = Namespace(
    'status', description='Get current status application')


@status_namespace.route('/')
class StatusResource(Resource):
    @status_namespace.doc(description='Retrieve the current status of the REST API application.')
    def get(self):
        """Get current status"""
        try:
            status = StatusModel.get_status()
            return jsonify(status)
        except Exception as ex:
            return jsonify({'message': str(ex)}), 500
