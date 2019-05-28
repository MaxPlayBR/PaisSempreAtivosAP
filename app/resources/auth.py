from flask_restful import Resource,marshal
from app.schemas import users_fields
from app import requests,db,app
from models import User,Medias
import jwt,json,base64
from requests import get
import datetime

class LoginRouter(Resource):
    def post(self):
        credential = requests.only(["matricula","password"]) 
        
        user = User.query.filter_by(matricula=credential["matricula"]).first()
        
        if not user or not user.compare_password(credential["password"]):
            return {"error":"Credenciais invalidas."},400
                
        payload = {
            "id":user.id,
            "exp":datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
        }
        try:
            token = jwt.encode(payload,app.config['SECRET_KEY'])
            return {"token":token.decode("utf-8")}
        except:
            return {"error":"Houve um erro ao tentar processar seu pedido"}
                    
class RegisterRouter(Resource):
    def post(self):
        url="http://aluno.seduc.ce.gov.br/api/dados_service/valida_login"
        credential = requests.only(["matricula","password"])   
        
        try:
            base = credential["matricula"]+":"+credential["password"]
            en = base64.b64encode(base.encode('ascii'))
            b64user = en.decode('ascii')
            
            headers={
                'Authorization':'Basic '+b64user,
                'User-Agent':'okhttp/3.3.0',
                'Accept-Encoding':'gzip',
                'Host':'aluno.seduc.ce.gov.br',
                'AppVersionName':'1.2',
                'AppVersionName':'4',
                'Accept':'application/json',
                'Cache-Control':'no-cache'
            }
            
            req = get(url,headers=headers).text
            
            if "message" in req:
                return {"error":"Matricula ou senha invalida."},400
                
            try:
                user = User(credential["matricula"],credential["password"])

                db.session.add(user)
                db.session.commit()
            except:
                return {"error":"O usuario já consta no banco de dados."},400
        
            return marshal(user,users_fields,"user"),200
        except Exception as e:
            print(credential)
            #return {"error":str(e)},500
            return {"error":"Matricula ou senha invalida."},500