from app.DAO.crud_departamentos import obtener_departamentos
from pandas import DataFrame
from DAO.crud_proyectos import ingresar_proyecto
class Proyecto():
    def __init__(self,id_departamento,id_proyecto,nombre,descripcion,fecha_inicio,estado):
        self.__id_departamento = id_departamento
        self.__id_proyecto = id_proyecto
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__fecha_inicio = fecha_inicio
        self.__estado = estado

    def get_id_departamento(self):
        return self.__id_departamento
    
    def set_id_departamento(self,id_proyecto):
        self.__id_departamento = id_proyecto

    def get_id_proyecto(self):
        return self.__id_proyecto
    
    def set_id_proyecto(self,id_proyecto):
        self.__id_proyecto = id_proyecto

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self._nombre = nombre

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre = nombre

    def get_descripcion(self):
        return self.__descripcion
    
    def set_descripcion(self,descripcion):
        self.__descripcion = descripcion

    def get_fecha_inicio(self):
        return self.__fecha_inicio
    
    def set_fecha_inicio(self,fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    def get_estado(self):
        return self.__estado
    
    def set_estado(self,estado):
        self.__estado = estado

    def __str__(self):
        txt = f" >> Proyecto {self.__id_proyecto}\n"
        txt += f"Nombre: {self.__nombre}\n"
        txt += f"Descripción: {self.__descripcion}\n"
        txt += f"Fecha de inicio: {self.__fecha_inicio}\n"
        txt += f"Estado: {self.__estado}\n"

        