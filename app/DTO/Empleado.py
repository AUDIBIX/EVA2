from app.DTO.Persona import Persona

class Empleado(Persona):
    def __init__(self, id_empleado, nombre, apellido_paterno, apellido_materno, rut, direccion, numero_telefonico, email, fecha_inicio_contrato, salario, nivel_acceso, password):
        super().__init__(id_empleado, nombre, apellido_paterno, apellido_materno, rut, direccion, numero_telefonico, email, fecha_inicio_contrato, salario, nivel_acceso, password)
    
    def __str__(self):
        txt = f" >> Empleado {self.get_id_empleado()} <<\n"
        txt+= super().__str__()
        return txt

    def crearRegistroDeTiempo(self,cantidad_horas,descripcion):
        pass
    
    def ver_registros():
        pass
    
    def ver_un_registro():
        pass
    
    def editar_registro():
        pass
    
    def eliminar_registro():
        pass