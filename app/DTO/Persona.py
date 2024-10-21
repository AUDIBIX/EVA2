from app.DAO.otros_dao import verificar_login
from app.DAO.crud_empleados import obtener_un_empleado
from pandas import DataFrame as DF
from app.DTO.Utiles import print_opciones
from app.DAO.crud_empleados import editar_usuario, editar_psw

class Persona:
    def __init__(self,id_empleado,nombre,apellido_paterno,apellido_materno,rut,direccion,numero_telefonico,email,fecha_inicio_contrato,salario:int,nivel_acceso,password):
        self.__id_empleado = id_empleado
        self.__nombre = nombre
        self.__apellido_paterno = apellido_paterno
        self.__apellido_materno = apellido_materno
        self.__rut = rut
        self.__direccion = direccion
        self.__numero_telefonico = numero_telefonico
        self.__email = email
        self.__fecha_inicio_contrato = fecha_inicio_contrato
        self.__salario = salario
        self.__nivel_acceso = nivel_acceso
        self.__password = password

    def get_id_empleado(self):
        return self.__id_empleado
    def get_nombre(self):
        return self.__nombre
    def get_apellido_paterno(self):
        return self.__apellido_paterno
    def get_apellido_materno(self):
        return self.__apellido_materno
    def get_rut(self):
        return self.__rut
    def get_direccion(self):
        return self.__direccion
    def get_numero_telefonico(self):
        return self.__numero_telefonico
    def get_email(self):
        return self.__email
    def get_fecha_inicio_contrato(self):
        return self.__fecha_inicio_contrato
    def get_salario(self):
        return self.__salario
    def get_nivel_acceso(self):
        return self.__nivel_acceso
    def get_password(self):
        return self.__password
    def get_apellido_paterno(self):
        return self.__apellido_paterno
    def get_apellido_materno(self):
        return self.__apellido_materno

    def set_id_empleado(self,id_empleado):
        self.__id_empleado = id_empleado
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def set_apellido_paterno(self,apellido_paterno):
        self.__apellido_paterno = apellido_paterno
    def set_apellido_materno(self,apellido_materno):
        self.__apellido_materno = apellido_materno
    def set_rut(self,rut):
        self.__rut = rut
    def set_direccion(self,direccion):
        self.__direccion = direccion
    def set_numero_telefonico(self,numero_telefonico):
        self.__numero_telefonico = numero_telefonico
    def set_email(self,email):
        self.__email = email
    def set_fecha_inicio_contrato(self,fecha_inicio_contrato):
        self.__fecha_inicio_contrato = fecha_inicio_contrato
    def set_salario(self,salario):
        self.__salario = salario
    def set_nivel_acceso(self,nivel_acceso):
        self.__nivel_acceso = nivel_acceso
    def set_password(self,password):
        self.__password = password
    def set_apellido_paterno(self,apellido_paterno):
        self.__apellido_paterno = apellido_paterno
    def set_apellido_materno(self,apellido_materno):
        self.__apellido_materno = apellido_materno
    

    def ver_perfil(id_usuario):
        try:
            datos_usuario = obtener_un_empleado(id_usuario)
            
            if datos_usuario is None:
                print("Usuario no encontrado.")
                return

            print(">>Perfil de Empleado<<")

            data_del_perfil = {
                'Nombre': f"{datos_usuario["nombre"]} {datos_usuario["apellido_paterno"]} {datos_usuario["apellido_materno"]}",
                'Direccion': f"{datos_usuario["direccion"]}",
                'Telefono': f"{datos_usuario["fono"]}",
                'Inicio De Contrato': f"{datos_usuario["fecha_inicio_contrato"]}",
                'Rol': f"{datos_usuario["nivel_acceso"]}",
                'Id del Departamento': f"{datos_usuario["id_departamento"]}"
            }

            print (DF([data_del_perfil]))  # Lista de un solo diccionario
            #print(df.to_string(index=False))  # Mostrar el DataFrame sin el índice

        except Exception as e:
            print(f"Error al mostrar la información: {e}")  
            #A.ver_info(usuario["id_empleado"])


    def editar_perfil(id_empleado): #contraseña,direccion,fono
        try:
            datos_usuario = obtener_un_empleado(id_empleado)
            
            if datos_usuario is None:
                print("Usuario no encontrado.")
                return
            
            print(f"Que datos desea Modificar >>{datos_usuario["nombre"]} {datos_usuario["apellido_paterno"]} {datos_usuario["apellido_materno"]}<<")

            print_opciones(["Contraseña","Direccion","Telefono"])
            question = input("> ")
            if question == '1':
                print("Cambio de Contraseña")

                try:
                    contraseña_actual = input("Ingrese su contraseña actual:\n> ")

                    if not verificar_login(id_empleado, contraseña_actual):
                        print("La contraseña actual no es correcta.")
                        return False

                    nueva_contraseña = input("Ingrese su nueva contraseña:\n> ")
                    confirmar_contraseña = input("Confirme su nueva contraseña:\n> ")

                    if nueva_contraseña != confirmar_contraseña:
                        print("Las nuevas contraseñas no coinciden.")
                        return False

                    if editar_psw(id_empleado, nueva_contraseña):
                        print(">> Contraseña cambiada con éxito <<")
                        return True
                    else:
                        print("Error al cambiar la contraseña.")
                        return False

                except Exception as e:
                    print(f"Error al cambiar la contraseña: {e}")
                    return False


            elif question == '2':
                print(f"Dirección actual: >>{datos_usuario['direccion']}<<")

                nueva_direccion = input("Ingrese nueva dirección:\n> ")

                if editar_usuario(id_empleado, "direccion", f"'{nueva_direccion}'"):
                    print("Dirección modificada con éxito.")


            elif question == '3':
                print(f"Teléfono actual: >>{datos_usuario['fono']}<<")

                nuevo_telefono = input("Ingrese nuevo teléfono:\n> ")

                if editar_usuario(id_empleado, "fono", f"'{nuevo_telefono}'"):
                    print("Teléfono modificado con éxito.")


            else:
                print("Opción no válida.")

        except Exception as e:
            print(f"Error al mostrar la información: {e}")




    def __str__(self):
        txt = f"Nombre completo: {self.__nombre} {self.__apellido_paterno} {self.__apellido_materno}\n"
        txt += f"Dirección: {self.__direccion}\n"
        txt += f"Número de teléfono: {self.__numero_telefonico}\n"
        txt += f"Correo electrónico: {self.__email}\n"
        txt += f"Fecha de inicio del contrato: {self.__fecha_inicio_contrato}\n"
        txt += f"Salario: {self.__salario}\n"
        txt += f"Nivel de acceso: {self.__nivel_acceso}\n"
        return txt
    


