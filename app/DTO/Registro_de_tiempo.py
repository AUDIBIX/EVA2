class Registro_de_tiempo():
    def __init__(self,id_registro,id_empleado,id_proyecto,fecha_registro,cantidad_horas,descripcion):
        self.__id_registro = id_registro
        self.__id_empleado = id_empleado
        self.__id_proyecto = id_proyecto
        self.__fecha_registro = fecha_registro
        self.__cantidad_horas = cantidad_horas
        self.__descripcion = descripcion
    
    def get_id_registro(self):
        return self.__id_registro
    def set_id_registro(self,id_registro):
        self.__id_registro = id_registro

    def get_id_empleado(self):
        return self.__id_empleado
    def set_id_empleado(self,id_empleado):
        self.__id_empleado = id_empleado

    def get_id_proyecto(self):
        return self.__id_proyecto
    def set_id_proyecto(self,id_proyecto):
        self.__id_proyecto = id_proyecto
        
    def get_fecha_registro(self):
        return self.__fecha_registro
    def set_fecha_registro(self,fecha_registro):
        self.__fecha_registro = fecha_registro
    
    def get_cantidad_horas(self):
        return self.__cantidad_horas
    def set_cantidad_horas(self,cantidad_horas):
        self.__cantidad_horas = cantidad_horas

    def get_descripcion(self):
        return self.__descripcion
    def set_descripcion(self,descripcion):
        self.__descripcion = descripcion

    def __str__(self):
        txt = " >> Registro de tiempo <<\n"
        txt += f"ID del registro: {self.__id_registro}\n"
        txt += f"ID del empleado: {self.__id_empleado}"
        txt += f"ID del proyecto: {self.__id_proyecto}\n"
        txt += f'Fecha del registro: {self.__fecha_registro}\n'
        txt += f"Cantidad de horas trabajadas: {self.__cantidad_horas}\n"
        txt += f"Descripción de las tareas realizadas: {self.__descripcion}"
        return txt