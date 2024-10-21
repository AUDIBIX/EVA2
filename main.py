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
                
                if accion == "1":
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
                    
            elif usuario.get_nivel_acceso() == "gerente":
                print(" Que desea hacer a continuación?")
                print_opciones(["Ver perfil","Levantar solicitud de asignacion de empleado a departamento","Designar un empleado a un proyecto","Editar un proyecto","Cerrar sesion","Salir"])
                accion = input("> ")
                
                if accion == "1":
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
                print_opciones(["Perfil","Crear registro","Cerrar sesion","Salir"])
                accion = input("> ")
                
                if accion == "1":
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
                    
                elif accion == "2":
                    E.crearRegistroDeTiempo()    
                
                elif accion == "3":
                    print("Cerrando sesión...")
                    sesion = False
                
                elif accion == "4":
                    print("Finalizando el programa...")
                    conexion.disconnect()
                    sesion = False
                    programa = False
                    
                
    
main()