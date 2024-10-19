class Solicitud():
    def __init__(self,id_solicitud,id_gerente,id_empleado,id_departamento,descripcion):
        self.__id_solicitud = id_solicitud
        self.__id_gerente = id_gerente
        self.__id_empleado = id_empleado
        self.__id_departamento = id_departamento
        self.__descripcion = descripcion

    def get_id_solicitud(self):
        return self.__id_solicitud
    
    def set_id_solicitud(self,id_solicitud):
        self.__id_solicitud = id_solicitud

    def get_id_gerente(self):
        return self.__id_gerente
    
    def set_id_gerente(self,id_gerente):
        self.__id_gerente = id_gerente

    def get_id_empleado(self):
        return self.__id_empleado
    
    def set_id_empleado(self,id_empleado):
        self.__id_empleado = id_empleado

    def get_id_departamento(self):
        return self.__id_departamento
    
    def set_id_departamento(self,id_departamento):
        self.__id_departamento = id_departamento

    def get_descripcion(self):
        return self.__descripcion

    def set_descripcion(self,descripcion):
        self.__descripcion = descripcion

    def __str__(self):
        txt = f" >> Solicitud {self.__id_solicitud}\n"
        txt += f"ID del gerente: {self.__id_gerente}\n"
        txt += f"ID del empleado: {self.__id_empleado}\n"
        txt += f"ID del departamento: {self.__id_departamento}\n"
        txt += f"Descripción: {self.__descripcion}\n"
        return txt