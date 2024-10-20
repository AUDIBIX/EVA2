from app.DTO.main_dto import login
from app.DTO.Administrador import Administrador as A
from app.DAO.DB import conexion

def main():
    programa = True
    sesion = True
    while programa == True:
        print(" >> Inicio de Sesion <<")
        usuario = login()
        while sesion == True:
            if usuario["nivel_acceso"] == "administrador":
                print(f" >> Bienvenido {usuario['nombre']} {usuario['apellido_paterno']}! <<")
                print(" Que desea hacer a continuación?")
                opciones = ["Registrar Empleado", "Crear Departamento", "Editar Departamento","Cerrar sesión","Salir"]
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
                    print("Cerrando sesión...")
                    sesion = False
                elif accion == "5":
                    print("Finalizando el programa...")
                    conexion.disconnect()
                    sesion = False
                    programa = False
    
main()