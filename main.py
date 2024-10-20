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
                opciones = ["Empleados", "Departamentos", "Editar Departamento","Cerrar sesión","Salir"]
                for indice , opcion in enumerate(opciones, start=1):
                    print(f"{indice}. {opcion}")
                accion = input("> ")
                if accion == "1":
                    while True:
                        opciones = ["Registrar empleado","Mostrar empleados","Editar empleado","Eliminar empleado/s","Salir"]
                        print("Que desea hacer?")
                        for numero,opcion in enumerate(opciones,start=1):
                            print(f"{numero}. {opcion}")
                        accion = input("> ")
                        if accion == "1":
                            A.registrarEmpleado()
                        elif accion == "2":
                            A.mostrar_empleados()
                        elif accion == "3":
                            A.editar_empleado()
                        elif accion == "4":
                            pass
                        elif accion == "5":
                            break
                        else:
                            print("Porfavor seleccione una opcion valida")
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