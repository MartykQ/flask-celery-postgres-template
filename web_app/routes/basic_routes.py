"""
Definition of basic http routes
"""

from flask import Blueprint, jsonify

from web_app.tasks.tasks import healthcheck_task

basic_routes = Blueprint('basic_routes', __name__)


@basic_routes.route('/healthcheck', methods=['GET'])
def health_check_route():
    """Healthcheck route"""
    healthcheck_task.apply_async(countdown=2)

    return jsonify({
        'msg': 'Running...'
    }), 200
