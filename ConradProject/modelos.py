from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

usuarios = []

class Usuario(UserMixin):

    def __init__(self, id, nombre, correo, password, is_admin=False):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.password = generate_password_hash(password)
        self.is_admin = is_admin

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.email)


def get_usuario(correo):
    for usuario in usuarios:
        if usuario.email == correo:
            return usuario
    return None