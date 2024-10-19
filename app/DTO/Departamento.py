class Departamento():
    def __init__(self,id_departamento,nombre,id_gerente,descripcion,estado):
        self.__id_departamento = id_departamento
        self.__nombre = nombre
        self.__id_gerente = id_gerente
        self.__descripcion = descripcion
        self.__estado = estado

    def get_id_departamento(self):
        return self.__id_departamento
    
    def set_id_departamento(self,id_departamento):
        self.__id_departamento = id_departamento

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
    
    def get_id_gerente(self):
        return self.__id_gerente
    
    def set_id_gerente(self,id_gerente):
        self.__id_gerente = id_gerente

    def get_descripcion(self):
        return self.__descripcion
    
    def set_descripcion(self,descripcion):
        self.__descripcion = descripcion

    def get_estado(self):
        return self.__estado
    
    def set_estado(self,estado):
        self.__estado = estado

    def __str__(self):
        txt = f" >> Departamento {self.__id_departamento}<<\n"
        txt += f"Nombre: {self.__nombre}\n"
        txt += f"ID del gerente responsable: {self.__id_gerente}\n"
        txt += f"Descripción: {self.__descripcion}\n"
        txt += f"Estado: {self.__estado}\n"
        return txt