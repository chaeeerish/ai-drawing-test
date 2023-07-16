# standard library imports
import base64
import json

# Third party imports
from flask import (Blueprint, jsonify, redirect, request, session, url_for)
from flask_cors import CORS
from flask_restx import Api, Resource, reqparse, Namespace

# local application imports
from main.config.db_connect import db
from main.model.repository.user.user_repository import *
from main.service.tree.tree_service import *
from main.service.house.house_service import *
from main.service.character.character import *
from main.service.common import send_slack_notification

bp = Blueprint('draw', __name__, url_prefix='/')
api = Namespace('draw_controller', description='draw_controller')
CORS(bp, resources={r'*': {'origins': '*'}})

@api.route('/tree')
@bp.route('/tree', methods=['POST'])
def tree_controller():
    if request.method == 'POST':
        # request params
        params = request.get_json()
        # session settings
        set_up(params['id'], params['image'][22:], 1)
        call_tree_model(params['id'])
        # http response
        return jsonify({'id': params['id']}), 200
    else:
        return jsonify({'error': 'Invalid request method'}), 400 

@api.route('/house')    
@bp.route('/house', methods=['POST'])
def house_controller():
    if request.method == 'POST':
        # request params
        params = request.get_json()
        # session settings
        set_up(params['id'], params['image'][22:], 2)
        house_process(params['id'])
                
        # http response
        id = params['id']
        user = find_user(id)
        user_tree_result = find_user_tree_result(id)
        user_house_result = find_user_house_result(id)

        return jsonify({
            'name': user.name,
            'tree_image': 'data:image/png;base64,' + binary_to_string(user.tree_image),
            'house_image': 'data:image/png;base64,' + binary_to_string(user.house_image),
            'tree_result': {
                '나무 유형': result_index_to_json(TREE_TYPE_RESULT, user_tree_result.type),
                '나무 뿌리': result_index_to_json(TREE_ROOT_RESULT, user_tree_result.root),
                '나무 가지': result_index_to_json(TREE_BRANCH_RESULT, user_tree_result.branch),
                '나뭇잎': result_index_to_json(TREE_LEAF_RESULT, user_tree_result.leap),
                '나무 줄기': result_index_to_json(TREE_STEM_RESULT, user_tree_result.stem),
                '나무 크기': result_index_to_json(TREE_SIZE_RESULT, user_tree_result.size)
            },
            'house_result': {
                '집 유형': result_index_to_json(HOUSE_TYPE_RESULT, user_house_result.type),
                '집 지붕': result_index_to_json(HOUSE_ROOF_RESULT, user_house_result.roof),
                '집 문': result_index_to_json(HOUSE_DOOR_RESULT, user_house_result.door),
                '집 창문': result_index_to_json(HOUSE_WINDOW_RESULT, user_house_result.windows)
            },
            'character': user_tree_result.characters,
            'graph': [user_tree_result.figures_gen, 
                      user_tree_result.figures_con, 
                      user_tree_result.figures_hap, 
                      user_tree_result.figures_soc, 
                      user_tree_result.figures_hig]
            }), 200
    else:
        return jsonify({'error': 'Invalid request method'}), 400 

# 오류 핸들러
@bp.app_errorhandler(Exception)
def handle_error(error):
    send_slack_notification(error, request)

def set_up(id, img_str, step):
    save_session(id, step)
    img_binary = base64.b64decode(img_str) # type: bytes
    update_user_draw(id, img_binary, step)

def string_to_json(str):
    if str is not None and str is not '':
        tmpjson = json.loads(str)
        if len(tmpjson) == 0:
            return None
        else:
            return tmpjson
    else:
        return None

def save_session(id, step):
    session['id'] = id
    session['step'] = step

def binary_to_string(img_binary):
    img_base64 = base64.b64encode(img_binary)
    return img_base64.decode('utf-8')