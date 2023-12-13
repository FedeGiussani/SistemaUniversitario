from modules.Usuario import Usuario
import datetime


class UsuarioFinal(Usuario):

    def __init__(self, nombre_usuario, contrasena, ID, nombre, apellido, email, claustro):
        super().__init__(nombre_usuario, contrasena)
        self._nombre_usuario=nombre_usuario
        self._contrasena=contrasena
        self._ID=ID
        self.__nombre=nombre
        self.__apellido=apellido
        self.__email=email
        self.__claustro=claustro
        self.__departamento=0
        self.__reclamos_adheridos=[] #lista de ID de reclamos adheridos
        self.__reclamos_generados=[] #lista de ID de reclamos generados por el usuario

    
    def cambiar_datos_usuario(self, contrasena, dato_a_cambiar, nuevo_dato):
        if contrasena==self._contrasena:
            if dato_a_cambiar=="nombre":
                self.__nombre=nuevo_dato
            elif dato_a_cambiar=="contraseña":
                self.__apellido=nuevo_dato
            elif dato_a_cambiar=="email":
                self.__email=nuevo_dato
            elif dato_a_cambiar=="claustro":
                self.__claustro=nuevo_dato
            else:
                raise Exception("Ese dato no existe")
        else:
            raise Exception("Contraseña incorrecta")
        

    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_apellido(self) -> str:
        return self.__apellido
    
    def get_email(self) -> str:
        return self.__email
    
    def get_claustro(self) -> str:
        return self.__claustro
    
    def get_reclamos_adheridos(self) -> list:
        return self.__reclamos_adheridos
    
    def get_reclamos_generados(self) -> list:
        return self.__reclamos_generados
    
    def get_departamento(self):
        return self.__departamento