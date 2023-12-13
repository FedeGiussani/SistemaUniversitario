

class Reclamo():
    def __init__(self, ID) -> None:
        self.__estado="Pendiente"
        self.__ID=0
        self.__fechaHora=None
        self.__departamento=None
        self.__adherentes=0
        self.__imagen=None
        self.__descripcion=None

    def set_fechaHora(self, fechaHora):
        self.__fechaHora=fechaHora
        
    def cambiar_departamento(self, dpto_jefe, nuevo_dpto):
        if dpto_jefe=="Secretaría Técnica":
            self.__estado=nuevo_dpto
        else:
            raise Exception("El usuario no puede derivar el reclamo")
        
    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado=="Pendiente" or "En proceso" or "Resuelto" or "Inválido":
            self.__estado=nuevo_estado
        else:
            raise Exception("No se pudo modificar el estado")