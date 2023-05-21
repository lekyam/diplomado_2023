from flask import Blueprint, jsonify
from models.StatusModel import StatusModel

main = Blueprint('status-blueprint', __name__)


@main.route('/')
def get_status():
    try:
        status = StatusModel.get_status()
        return jsonify(status)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
