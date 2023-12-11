
class JefeDepartamento():
    def __init__(self):
        self.__departamento = "Secretaria Técnica"

    def set_departamento(self, dpto):
        self.__departamento=dpto

    def get_departamento(self):
        return self.__departamento