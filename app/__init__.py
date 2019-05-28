import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)),"app.db")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:////{basedir}"
app.config['SECRET_KEY'] = b'\xb4\xa9\xe7x\x8aL*K\xb9l\xbf\n\xe7\xe4\x85\x95\x8d\x040\x8b!\xe0\xed\x87'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app,prefix="/api/v1")
db = SQLAlchemy(app)
CORS(app)

from app.resources.auth import LoginRouter,RegisterRouter
api.add_resource(RegisterRouter,"/register")
api.add_resource(LoginRouter,"/login")

from app.resources.boletim import BoletimRouter
api.add_resource(BoletimRouter,"/medias")

from app.resources.atualizar import AtualizarRouter
api.add_resource(AtualizarRouter,"/atualizar")