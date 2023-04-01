# standard library imports
import base64
import json
# Third party imports
from flask import (Blueprint, jsonify, redirect, request, session, url_for)
from flask_cors import CORS
# local application imports
from main.config.db_connect import db
from main.model.repository.user.user_repository import *
from main.service.draw.tree_service import *
from main.service.draw.house_service import *

bp = Blueprint('draw', __name__, url_prefix='/')
CORS(bp, resources={r"*": {"origins": "*"}})

@bp.route('/tree/', methods=['POST', 'GET'])
def tree_draw_save():
    if request.method == 'POST':
        # request params
        params = request.get_json()
        # session settings
        setup(params['userid'], params['image'][22:], 1)
        call_tree_model(params['userid'])
        # http response
        return jsonify({'message': 'The tree image is saved.', "userid": params['userid'] }), 200
    
@bp.route('/home/', methods=['POST', 'GET'])
def house_draw_save():
    if request.method == 'POST':
        # request params
        params = request.get_json()
        # session settings
        setup(params['userid'], params['image'][22:], 2)
        house_process(params['userid'])
        
        # http response
        userid = params['userid']
        user = find_user(userid)
        user_tree = find_user_tree_result(userid)
        user_house = find_user_house_result(userid)

        return jsonify({
            "username": user.username,
            "image1": 'data:image/png;base64,' + binary_to_string(user.treeimg),
            "image2": 'data:image/png;base64,' + binary_to_string(user.houseimg),
            "tree": {
                "나무 유형": string_to_json(user_tree.treetype),
                "나무 뿌리": string_to_json(user_tree.treeroot),
                "나무 가지": string_to_json(user_tree.treebranch),
                "나뭇잎": string_to_json(user_tree.treeleap),
                "나무 줄기": string_to_json(user_tree.treestem),
                "나무 크기": string_to_json(user_tree.treesize)
            },
            "home": {
                "집 유형": string_to_json(user_house.housetype),
                "집 지붕": string_to_json(user_house.houseroof),
                "집 문": string_to_json(user_house.housedoor),
                "집 창문": string_to_json(user_house.housewindow)
            }
        }), 200
    
def binary_to_string(img_binary):
    img_base64 = base64.b64encode(img_binary)
    return img_base64.decode('utf-8')

def setup(userid, img_str, step):
    save_session(userid, step)
    img_binary = base64.b64decode(img_str) # type: bytes
    update_user_draw(userid, img_binary, step)

def string_to_json(str):
    if str is not None and str is not "":
        tmpsjon = json.loads(str)
        if len(tmpsjon) == 0:
            return None
        else:
            return tmpsjon
    else:
        return None

def save_session(userid, step):
    session['userid'] = userid
    session['step'] = step