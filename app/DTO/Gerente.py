from app.DTO.Persona import Persona

class Gerente(Persona):
    def __init__(self, id_empleado, nombre, apellido_paterno, apellido_materno, rut, direccion, numero_telefonico, email, fecha_inicio_contrato, salario, nivel_acceso, password):
        super().__init__(id_empleado, nombre, apellido_paterno, apellido_materno, rut, direccion, numero_telefonico, email, fecha_inicio_contrato, salario, nivel_acceso, password)
    
    def __str__(self):
        txt = f" >> Gerente {self.__id_empleado} <<\n"
        txt+= super().__str__
        return txt
    
    def levantarSolicitudEmpleadoDepartamento(id_gerente,id_empleado,descripcion):
        pass

    def designarEmpleadoProyecto(id_empleado,accion,id_proyecto):
        pass

    def editarProyecto(id_proyecto,atributo,valor):
        pass