from app import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    matricula = db.Column(db.String(20),nullable=False,unique=True, index=True)
    password = db.Column(db.String(180),nullable=False)
    def __init__(self,matricula,password):
        self.matricula = matricula
        self.password = generate_password_hash(password)
        
    def compare_password(self,password):
        return check_password_hash(self.password,password)
        
        
    def __repr__(self):
        return f'<User self.matricula'


class Medias(db.Model):
    __tablename__="medias"
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    matricula = db.Column(db.String(20),nullable=False,unique=True, index=True)
    faltas = db.Column(db.String(300),nullable=False)
    mediaBaixa = db.Column(db.String(600),nullable=False)
    
    def __init__(self,matricula,mediaBaixa,faltas):
        self.matricula = matricula
        self.mediaBaixa = mediaBaixa
        self.faltas = faltas
        
    def __repr__(self):
        return f'<User self.matricula'