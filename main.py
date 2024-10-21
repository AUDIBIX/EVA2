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
                opciones = ["Perfil","Empleados", "Departamentos", "Cerrar sesión", "Salir"]
                print_opciones(opciones)
                accion = input("> ")
                
                if accion == "1":
                    while True:
                        print("Que desea hacer?")
                        print_opciones(["Mostrar perfil","Editar perfil","Salir","PRUEBA"])
                        accion = input("> ")
                        if accion == "1":
                            A.ver_perfil(usuario["id_empleado"])
                        elif accion == "2":
                            A.editar_perfil(usuario["id_empleado"])
                        elif accion == "3":
                            break
                        elif accion == "4": #prueba
                            A.crearProyecto
                        else:
                            print("Porfavor seleccione una opcion valida")
                
                if accion == "2":
                    while True:
                        print("Que desea hacer?")
                        print_opciones(["Registrar empleado","Mostrar empleados","Editar empleado","Eliminar empleado/s","Salir"])
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
                        else:
                            print("Porfavor seleccione una opcion valida")
                            
                elif accion == "3":
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
                        
                elif accion == "4":
                    print("Cerrando sesión...")
                    sesion = False
                    
                elif accion == "5":
                    print("Finalizando el programa...")
                    conexion.disconnect()
                    sesion = False
                    programa = False
                
                else:
                    print("Porfavor seleccione una opcion valida")
    
main()