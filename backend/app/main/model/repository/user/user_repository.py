from main.config.db_connect import db
from main.model.domain.user.user_model import *

def save_user(name):
    user = UserImage(name=name)
    db.session.add(user)
    db.session.commit()
    return user.id

def save_user_tree_result(id, result_cls):
    result_db = UserTreeResult(id=id)
    result_db.type = result_cls.type
    result_db.root = result_cls.root
    result_db.branch = result_cls.branch
    result_db.leap = result_cls.leap
    result_db.stem = result_cls.stem
    result_db.size = result_cls.size
    result_db.characters = result_cls.character
    result_db.figures_gen = result_cls.figures_gen
    result_db.figures_con = result_cls.figures_con
    result_db.figures_hap = result_cls.figures_hap
    result_db.figures_soc = result_cls.figures_soc
    result_db.figures_hig = result_cls.figures_hig
    db.session.add(result_db)
    db.session.commit()

def save_user_house_result(id, result_cls):
    result_db = UserHouseResult(id=id)
    result_db.type = result_cls.type
    result_db.roof = result_cls.roof
    result_db.door = result_cls.door
    result_db.windows = result_cls.window
    db.session.add(result_db)
    db.session.commit()

def find_user(id):
    return db.session.query(UserImage).filter(UserImage.id == id).first()

def find_user_tree_result(id):
    return db.session.query(UserTreeResult).filter(UserTreeResult.id == id).first()

def find_user_house_result(id):
    return db.session.query(UserHouseResult).filter(UserHouseResult.id == id).first()

def update_user_draw(id, img_binary, step):
    user = find_user(id)
    if step == 1:
        user.tree_image = img_binary
    elif step == 2:
        user.house_image = img_binary
    db.session.commit()
