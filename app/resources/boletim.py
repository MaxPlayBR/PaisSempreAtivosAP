from flask_restful import Resource,marshal
from models import Medias
from app import requests
from app.schemas import boletim_fields
from app.decorator import jwt_required

class BoletimRouter(Resource):
    @jwt_required
    def post(self,current_user):
        hd = requests.only(["matricula"])        
        notas = Medias.query.filter_by(matricula=hd["matricula"]).first()
        
        return marshal(notas,boletim_fields,"Medias")
        