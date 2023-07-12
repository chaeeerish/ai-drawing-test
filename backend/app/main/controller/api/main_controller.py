# standard library imports

# Third party imports
from flask import (Blueprint, jsonify, request, session)
from flask_cors import CORS
from flask_restx import Api, Resource, reqparse, Namespace

# local application imports
from main.config.db_connect import db
from main.model.repository.user.user_repository import *
from main.service.common import send_slack_notification

bp = Blueprint('main', __name__, url_prefix='/')
CORS(bp, resources={r"*": {"origins": "*"}})

api = Namespace('main_controller', description='main_controller')

@api.route('/main')
@bp.route('/main', methods=['POST'])
def show_main_page():
    if request.method == 'POST':
        params = request.get_json()
        session['id'] = save_user(params['name'])
        return jsonify({'id': session['id']}), 200
    else:
        return jsonify({'error': 'Invalid request method'}), 400 

# 오류 핸들러
@bp.app_errorhandler(Exception)
def handle_error(error):
    send_slack_notification(error, request)
