from modules.Usuario import Usuario

class JefeDepartamento(Usuario):
    def __init__(self, nombre_usuario, contrasena, ID):
        super().__init__(nombre_usuario, contrasena)
        self._ID=ID
        self.__departamento=None

    def set_departamento(self, departamento):
        self.__departamento=departamento

    def get_departamento(self):
        return self.__departamento