from Persona import Persona

class Gerente(Persona):
    def __init__(self, nombre, apellido_paterno, apellido_materno, direccion, numero_telefonico, email, fecha_inicio_contrato, salario: float, nivel_acceso: int, contrasena, id_gerente):
        super().__init__(nombre, apellido_paterno, apellido_materno, direccion, numero_telefonico, email, fecha_inicio_contrato, salario, nivel_acceso, contrasena)
        self.__id_gerente = id_gerente
    
    def get_id_gerente(self):
        return self.__id_gerente
    
    def set_id_gerente(self,id_gerente):
        self.__id_gerente = id_gerente

    def __str__(self):
        txt = f" >> Gerente {self.__id_gerente} <<\n"
        txt+= super().__str__
        return txt
    
    def levantarSolicitudEmpleadoDepartamento(id_gerente,id_empleado,descripcion):
        pass

    def designarEmpleadoProyecto(id_empleado,accion,id_proyecto):
        pass

    def editarProyecto(id_proyecto,atributo,valor):
        pass