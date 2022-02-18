from urllib.parse import uses_query
import uuid

class Usuario:
    def __init__(self, nombres, apellidos, edad, email):
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad
        self.email = email
        self.id = str(uuid.uuid4())
    
    def setter(self, n_nombre, n_appellidos, n_edad, n_email):
        self.nombres = n_nombre
        self.apellidos = n_appellidos
        self.edad = n_edad
        self.email = n_email

    def __repr__(self) -> str:
        return "Nombre: {nomb} , Apellidos: {apellidos} , Edad: {edad} , Email: {email}".\
            format(nomb = self.nombres, apellidos = self.apellidos, edad= self.edad, email = self.email)

class Modelo:
    def __init__(self):
        self.dictionary = {}

    def add_user(self, usuario):
        self.dictionary [usuario.id ] = usuario

    def get_users(self):
        return list(self.dictionary.values())
    
    def update_user(self, _id, nombre, apellidos, edad, email):
        usuario = self.dictionary[_id]
        usuario.setter(nombre, apellidos, edad, email)
    
    def delete_user(self, _id):
        del self.dictionary[_id]


m = Modelo()
print(m.get_users())
u = Usuario("nomb", "appell", 22, "a@a")
m.add_user(u)
print(m.get_users())
m.update_user(u.id, "nuevo", "nuevo", 11, "n@n")
print(m.get_users())
m.delete_user(u.id)
print(m.get_users())