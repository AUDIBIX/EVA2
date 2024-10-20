from app.DTO.Persona import Persona
from app.DTO.Empleado import Empleado
from app.DTO.Departamento import Departamento
from app.DAO.ingresar_dao import ingresar_empleado,ingresar_departamento
from app.DAO.editar_dao import editar_departamento
from app.DAO.obtener_dao import obtener_departamentos,obtener_informacion_departamento,obtener_gerentes,obtener_empleados
from app.DAO.eliminar_dao import eliminar_usuario
from app.DTO.Utiles import print_opciones
from random import randint
from pandas import DataFrame

class Administrador(Persona):
    def __init__(self, id_empleado, nombre, apellido_paterno, apellido_materno, rut, direccion, numero_telefonico, email, fecha_inicio_contrato, salario, nivel_acceso, password):
        super().__init__(id_empleado, nombre, apellido_paterno, apellido_materno, rut, direccion, numero_telefonico, email, fecha_inicio_contrato, salario, nivel_acceso, password)

    def registrarEmpleado():
        print(" >> Creación de empleado <<")
        nombre = input("Ingrese nombre:\n> ")
        apellido_paterno = input("Ingrese apellido paterno:\n> ")
        apellido_materno = input("Ingrese apellido materno:\n> ")
        rut = input("Ingrese rut:\n> ")
        email = f"{nombre.lower()}.{apellido_paterno.lower()}{randint(0,99)}@ecotech.cl"
        salario = input("Ingrese salario:\n> ")
        question = input("Desea asignar el nivel de acceso? s/n\n> ")
        if question == "s":
            print("Ingrese el nivel de acceso:")
            print_opciones(["Empleado","Gerente","Administrador"])
            question = input("> ")
            if question == "1":
                nivel_acceso = "empleado"
            elif question == "2":
                nivel_acceso = "gerente"
            elif question == "3":
                nivel_acceso = "administrador"
        else:
            nivel_acceso = "empleado"
        question = input("Desea agregar una dirección? s/n\n> ")
        direccion = "Null"
        if question == "s":
            direccion = input("Ingrese dirección:\n> ")
        question = input("Desea agregar un fono? s/n\n> ")
        fono = "Null"
        if question == "s":
            fono = input("Ingrese fono:\n> ")
        if ingresar_empleado(nombre,apellido_paterno,apellido_materno,direccion,fono,salario,nivel_acceso,rut,email,psw="12345"):
            print("Empleado creado correctamente")
            
    
    def mostrar_empleados():
        empleados = obtener_empleados()
        cambios = {
            "id_empleado": "ID",
            "nombre": "Nombre",
            "apellido_paterno": "Apellido paterno",
            "apellido_materno": "Apellido materno",
            "direccion": "Direccion",
            "fono": "Numero telefonico",
            "fecha_inicio_contrato": "Inicio de contrato",
            "salario": "Salario",
            "nivel_acceso": "Rol",
            "rut": "Run",
            "id_departamento": "ID de departamento",
            "email": "E-Mail"
        }
        for empleado in empleados:
            for clave_antigua,clave_nueva in cambios.items():
                empleado[clave_nueva] = empleado.pop(clave_antigua)
        print(">> Empleados")
        print(DataFrame(empleados))
    
    
    def editar_empleado():
        Administrador.mostrar_empleados()
        print("Ingrese el ID del empleado a editar:")
        id = input("> ")
    

    def eliminar_empleado():
        Administrador.mostrar_empleados()
        print("Ingrese el ID del empleado a eliminar")
        id = input("> ")
        if eliminar_usuario(id):
            print("Empleado eliminado con exito")
    
    
    def crearDepartamento():
        print(" >> Creacion de departamento <<")
        nombre = input("Ingrese nombre:\n> ")
        descripcion = input("Ingrese descripcion:\n> ")
        id_empleado = None
        question = input("Desea asignar un gerente? s/n\n> ")
        if question == "s":
            print("Gerentes sin departamento asignado:")
            print(DataFrame(obtener_gerentes()))
            id_empleado = input("Ingrese el ID del gerente:\n> ")
        print("Ingrese el estado inicial del departamento:")
        print("1. Inactivo")
        print("2. Activo")
        estado = input("> ")
        if estado == "1":
            estado = "Inactivo"
        elif estado == "2":
            estado = "Activo"
        else:
            estado = None
        objeto_departamento = Departamento(None,nombre,id_empleado,descripcion,estado)
        if ingresar_departamento(objeto_departamento):
            print("Departamento creado correctamente")
    
    
    def mostrar_departamentos():
        print(">> Departamentos")
        departamentos = obtener_departamentos()
        cambios = {
            "id_departamento": "ID",
            "id_gerente": "Gerente asignado",
            "nombre": "Nombre",
            "descripcion": "Descripcion",
            "estado": "Estado"
        }
        for departamento in departamentos:
            for clave_antigua,clave_nueva in cambios.items():
                departamento[clave_nueva] = departamento.pop(clave_antigua)
        print(DataFrame(departamentos))
        

    def editarDepartamento(): #Faltan validaciones
        Administrador.mostrar_departamentos()
        id_departamento = input("Ingrese el ID\n> ")
        
        while True:
            if depto := obtener_informacion_departamento(id_departamento):
                print(f" >> Departamento {depto["Nombre"]} <<")
                for key,item in depto.items():
                    print(f"{key}: {item}")
            else:
                break
            print("Que desea modificar?")
            print_opciones(["Gerente asignado","Nombre","Descripción","Estado","Salir"])
            accion = input("> ")
            if accion == "1":
                if gerentes := obtener_gerentes():
                    print(">> Gerentes sin asignar <<")
                    print(DataFrame(gerentes))
                else:
                    print("No hay gerentes disponibles")
                    break
                nuevo_valor = input("Ingrese el ID del nuevo gerente\n> ")
                if editar_departamento(id_departamento,"id_gerente",nuevo_valor):
                    print("Edicion realizada con exito")
            elif accion == "2":
                pass
            elif accion == "3":
                pass
            elif accion == "4":
                pass
            elif accion == "5":
                break
            else:
                print("Porfavor ingrese una opcion valida")
        
    
    def buscarDepartamento(id_departamento):
        pass

    
    def removerDepartamento(id_departamento):
        pass

    
    def aprobarSolicitud(id_solicitud):
        pass

    
    def generarInforme(formato,datos_empleados,datos_proyectos,datos_departamentos,datos_registros_de_tiempo):
        pass

    
    def crearProyecto(nombre,descripcion):
        pass

    
    def editarProyecto(id_proyecto,campo,valor):
        pass

    
    def eliminarProyecto(id_proyecto):
        pass

    def __str__(self):
        txt = f" >> Administrador {self.__id_empleado} <<\n"
        txt += Persona().__str__()
        return txt