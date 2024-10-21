from app.DTO.Empleado import Empleado
from app.DAO.crud_empleados import obtener_un_empleado
def login():
    intentos = 0
    while intentos < 3:
        print("Ingrese su ID:")
        id = input("> ")
        print("Ingrese contraseña:")
        contrasena = input("> ")
        if usuario := obtener_un_empleado(id):
            if usuario["psw"] == contrasena:
                empleado = Empleado(usuario["id_empleado"],usuario["nombre"],usuario["apellido_paterno"],usuario["apellido_materno"],usuario["rut"],usuario["direccion"],usuario["fono"],usuario["email"],usuario["fecha_inicio_contrato"],usuario["salario"],usuario["nivel_acceso"],usuario["psw"])
                return empleado
        intentos += 1
        print("Usuario o contraseña incorrectos, intente nuevamente")