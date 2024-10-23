from app.DTO.main_dto import login
from app.DTO.Administrador import Administrador as A
from app.DTO.Gerente import Gerente as G
from app.DTO.Empleado import Empleado as E
from app.DAO.DB import conexion
from app.DTO.Utiles import print_opciones

def main():
    programa = True
    while programa == True:
        print(" >> Inicio de Sesion <<")
        usuario = login()
        sesion = True
        while sesion == True:
            print(f" >> Bienvenido {usuario.get_nombre()} {usuario.get_apellido_paterno()}! <<")
            if usuario.get_nivel_acceso() == "administrador":
                print(" Que desea hacer a continuación?")
                print_opciones(["Perfil","Empleados", "Departamentos", "Cerrar sesión", "Salir"])
                accion = input("> ")
                
                if accion == "1":#Menu perfil
                    while True:
                        print("Que desea hacer?")
                        print_opciones(["Mostrar perfil","Editar perfil","Salir"])
                        accion = input("> ")
                        if accion == "1":
                            A.ver_perfil(usuario.get_id_empleado())
                        elif accion == "2":
                            A.editar_perfil(usuario.get_id_empleado())
                        elif accion == "3":
                            break
                        else:
                            print("Porfavor seleccione una opcion valida")
                
                elif accion == "2":#Menu empleados
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
                
                elif accion == "3":#Departamentos
                    while True:
                        print("Que desea hacer?")
                        print_opciones(["Crear departamento","Mostrar departamentos","Editar departamento","Eliminar departamento","Salir"])
                        accion = input("> ")
                        if accion == "1":
                            A.crearDepartamento()
                        elif accion == "2":
                            A.mostrar_departamentos()
                        elif accion == "3":
                            A.editarDepartamento()
                        elif accion == "4":
                            A.eliminarDepartamento()
                        elif accion == "5":
                            break
                        else:
                            print("Porfavor seleccione una opcion valida")
                
                elif accion == "4":#Cierre sesión
                    print("Cerrando sesión...")
                    sesion = False
                
                elif accion == "5":#Cierre programa
                    print("Finalizando el programa...")
                    conexion.disconnect()
                    sesion = False
                    programa = False

                else:
                    print("Porfavor seleccione una opcion valida")
                    
            elif usuario.get_nivel_acceso() == "gerente":
                print(" Que desea hacer a continuación?")
                print_opciones(["Ver perfil","Levantar solicitud de asignacion de empleado a departamento","Designar un empleado a un proyecto","Editar un proyecto","Cerrar sesion","Salir"])
                accion = input("> ")
                
                if accion == "1":
                    while True:#Menu perfil
                        print("Que desea hacer?")
                        print_opciones(["Mostrar perfil","Editar perfil","Salir"])
                        accion = input("> ")
                        if accion == "1":
                            A.ver_perfil(usuario.get_id_empleado())
                        elif accion == "2":
                            A.editar_perfil(usuario.get_id_empleado())
                        elif accion == "3":
                            break
                        else:
                            print("Porfavor seleccione una opcion valida")
                
                elif accion == "2":
                    G.levantarSolicitudEmpleadoDepartamento()
                elif accion == "3":
                    G.designarEmpleadoProyecto()
                elif accion == "4":
                    G.editarProyecto()
                    
                elif accion == "5":
                    print("Cerrando sesión...")
                    sesion = False
                
                elif accion == "6":
                    print("Finalizando el programa...")
                    conexion.disconnect()
                    sesion = False
                    programa = False
                    
                else:
                    print("Seleccione una opcion valida")
                
            elif usuario.get_nivel_acceso() == "empleado":
                print("Que desea hacer?")
                print_opciones(["Perfil","Registros de tiempo","Cerrar sesion","Salir"])
                accion = input("> ")
                
                if accion == "1":#Menu perfil
                    while True:
                        print("Que desea hacer?")
                        print_opciones(["Ver perfil","Modificar perfil","Salir"])
                        accion == input("> ")
                        if accion == "1":
                            E.ver_perfil()
                        elif accion == "2":
                            E.editar_perfil()
                        elif accion == "3":
                            break
                    
                elif accion == "2":#Menu registro de tiempo
                    while True:
                        print("Que desea hacer?")
                        print_opciones(["Crear registro","Ver registros","Ver un registro","Modificar registro","Eliminar registro","Salir"])
                        accion = input("> ")
                        if accion == "1":
                            E.crearRegistroDeTiempo()
                        elif accion == "2":
                            E.ver_registros()
                        elif accion == "3":
                            E.ver_un_registro()
                        elif accion == "4":
                            E.editar_registro()
                        elif accion == "5":
                            E.eliminar_registro()
                        elif accion == "6":
                            break
                        else:
                            print("Seleccione una accion valida")
                
                elif accion == "3":
                    print("Cerrando sesión...")
                    sesion = False
                
                elif accion == "4":
                    print("Finalizando el programa...")
                    conexion.disconnect()
                    sesion = False
                    programa = False


main()