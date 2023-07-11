from main.config.db_connect import db
from sqlalchemy.dialects.postgresql import ARRAY

class UserImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    tree_image = db.Column(db.BLOB)
    house_image = db.Column(db.BLOB)

class UserTreeResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.TEXT)
    root = db.Column(db.TEXT)
    branch = db.Column(db.TEXT)
    leap = db.Column(db.TEXT)
    stem = db.Column(db.TEXT)
    size = db.Column(db.TEXT)
    characters = db.Column(db.Integer)
    figures_gen = db.Column(db.FLOAT)
    figures_con = db.Column(db.FLOAT)
    figures_hap = db.Column(db.FLOAT)
    figures_soc = db.Column(db.FLOAT)
    figures_hig = db.Column(db.FLOAT)

class UserHouseResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.TEXT)
    roof = db.Column(db.TEXT)
    door = db.Column(db.TEXT)
    windows = db.Column(db.TEXT)
	