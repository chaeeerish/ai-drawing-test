# standard library imports
import os
# Third party imports
from flask import Flask
from flask_cors import CORS
# local application imports
from main.config.db_connect import db
from main.controller.api.draw_controller import bp as drawbp
from main.controller.api.main_controller import bp as mainbp
# from dotenv import load_dotenv

# load_dotenv()

# print("******************")
# print(os.environ.get('AWS_ACCESS_KEY_ID'))
# print(os.environ.get('AWS_SECRET_ACCESS_KEY'))
# print("******************")

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

aws_db = {
    'host': os.environ.get('RDS_HOST'),
    'port': os.environ.get('RDS_PORT'),
    'user': os.environ.get('RDS_USERNAME'),
    'password': os.environ.get('RDS_PASSWORD'),
    'database': os.environ.get('RDS_DATABASE')
}

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{aws_db['user']}:{aws_db['password']}@{aws_db['host']}:{aws_db['port']}/{aws_db['database']}?charset=utf8"
print(aws_db)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLARCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.environ.get('SECRET_KEY')

db.init_app(app)

app.register_blueprint(mainbp)
app.register_blueprint(drawbp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
