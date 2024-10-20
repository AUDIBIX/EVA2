class Informe():
    def __init__(self,formato,datos_empleados,datos_proyectos,datos_departamentos,datos_registros_de_tiempo,fecha_informe):
        self.__formato = formato
        self.__datos_empleados = datos_empleados
        self.__datos_proyectos = datos_proyectos
        self.__datos_departamentos = datos_departamentos
        self.__datos_registros_de_tiempo = datos_registros_de_tiempo
        self.__fecha_informe = fecha_informe

    def get_formato(self):
        return self.__formato
    def set_formato(self,formato):
        self.__formato = formato

    def get_datos_empleados(self):
        return self.__datos_empleados
    def set_datos_empleados(self,datos_empleados):
        self.__datos_empleados = datos_empleados
        
    def get_datos_proyectos(self):
        return self.__datos_proyectos
    def set_datos_proyectos(self,datos_proyectos):
        self.__datos_proyectos = datos_proyectos
    
    def get_datos_departamentos(self):
        return self.__datos_departamentos
    def set_datos_departamentos(self,datos_departamentos):
        self.__datos_departamentos = datos_departamentos

    def get_datos_registros_de_tiempo(self):
        return self.__datos_registros_de_tiempo
    def set_datos_registros_de_tiempo(self,datos_registros_de_tiempo):
        self.__datos_registros_de_tiempo = datos_registros_de_tiempo
    
    def get_fecha_informe(self):
        return self.__fecha_informe
    def set_fecha_informe(self,fecha_informe):
        self.__fecha_informe = fecha_informe