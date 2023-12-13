from abc import ABC, abstractmethod

class Usuario(ABC):

    @abstractmethod
    def __init__(self, nombre_usuario, contrasena):
        self._nombre_usuario=nombre_usuario
        self._contrasena=contrasena
        self._ID=None

    def cambiar_datos(self, contrasena, dato_a_cambiar, nuevo_dato):
        if contrasena==self._contrasena:
            if dato_a_cambiar=="nombre_usuario":
                self._nombre_usuario=nuevo_dato
            elif dato_a_cambiar=="contraseña":
                self._contrasena=nuevo_dato
            else:
                raise Exception("Ese dato no existe")
        else:
            raise Exception("Contraseña incorrecta")
    
    def set_ID(self, ID):
        self._ID=ID

    def get_ID(self, ID):
        return self._ID
        
    def get_nombre_usuario(self):
        return self._nombre_usuario

    def get_nombre_usuario(self):
        return self._contrasena