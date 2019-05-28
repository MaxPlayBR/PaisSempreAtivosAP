from flask_restful import fields

users_fields = {
    "id":fields.Integer,
    "matricula":fields.String
}

boletim_fields = {
    "id":fields.Integer,
    "faltas":fields.Integer,
    "mediaBaixa":fields.String,
}