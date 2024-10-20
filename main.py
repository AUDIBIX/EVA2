from app.DTO.main_dto import login
from app.DTO.Administrador import Administrador as A
from app.DAO.DB import conexion
from app.DTO.Utiles import print_opciones

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
                print_opciones(["Empleados", "Departamentos", "Cerrar sesión", "Salir"])
                accion = input("> ")
                
                if accion == "1":
                    while True:
                        print("Que desea hacer?")
                        print_opciones(["Registrar empleado","Mostrar empleados","Editar empleado","Eliminar empleado/s","Salir","Prueba editar perfil"])
                        accion = input("> ")
                        if accion == "1":
                            A.registrarEmpleado()
                        elif accion == "2":
                            A.mostrar_empleados()
                        elif accion == "3":
                            A.editar_empleado()
                        elif accion == "4":
                            A.eliminar_empleado()
                        elif accion == "5":
                            break
                        elif accion == "6":
                            A.editar_perfil(usuario["id_empleado"]) #prueba editar perfil
                        else:
                            print("Porfavor seleccione una opcion valida")
                            
                elif accion == "2":
                    while True:
                        print_opciones(["Crear departamento","Mostrar departamentos","Editar departamento","Eliminar departamento","Salir"])
                        accion = input("> ")
                        if accion == "1":
                            A.crearDepartamento()
                        elif accion == "2":
                            A.mostrar_departamentos()
                        elif accion == "3":
                            A.editarDepartamento()
                        elif accion == "4":
                            pass
                        elif accion == "5":
                            break
                        else:
                            print("Porfavor seleccione una opcion valida")
                        
                elif accion == "3":
                    print("Cerrando sesión...")
                    sesion = False
                    
                elif accion == "4":
                    print("Finalizando el programa...")
                    conexion.disconnect()
                    sesion = False
                    programa = False
                
                else:
                    print("Porfavor seleccione una opcion valida")
    
main()