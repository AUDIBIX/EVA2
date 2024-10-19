from app.DTO.main_dto import login
from app.DTO.Administrador import Administrador as A
from app.DAO.DB import conexion

def main():
    while True:
        print(" >> Inicio de Sesion <<")
        usuario = login()
        if usuario["nivel_acceso"] == "administrador":
            print(f" >> Bienvenido {usuario['nombre']} {usuario['apellido_paterno']}! <<")
            print(" Que desea hacer a continuación?")
            opciones = ["Registrar Empleado", "Crear Departamento", "Editar Departamento","Cerrar sesión"]
            for indice , opcion in enumerate(opciones, start=1):
                print(f"{indice}. {opcion}")
            accion = input("> ")
            if accion == "1":
                A.registrarEmpleado()
            elif accion == "2":
                A.crearDepartamento()
            elif accion == "3":
                A.editarDepartamento()
            elif accion == "4":
                conexion.disconnect()
                continue
    
main()