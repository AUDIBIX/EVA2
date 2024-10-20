from app.DTO.Persona import Persona
from app.DTO.Empleado import Empleado
from app.DTO.Departamento import Departamento
from app.DAO.ingresar_dao import ingresar_empleado,ingresar_departamento
from app.DAO.editar_dao import departamento_editar_descripcion, departamento_editar_estado, departamento_editar_id_empleado, departamento_editar_nombre
from app.DAO.obtener_dao import obtener_departamentos,obtener_informacion_departamento
from app.DTO.Utiles import print_opciones
from random import randint
from pandas import DataFrame

class Administrador(Persona):
    def __init__(self, id_empleado, nombre, apellido_paterno, apellido_materno, rut, direccion, numero_telefonico, email, fecha_inicio_contrato, salario, nivel_acceso, password):
        super().__init__(id_empleado, nombre, apellido_paterno, apellido_materno, rut, direccion, numero_telefonico, email, fecha_inicio_contrato, salario, nivel_acceso, password)

    def registrarEmpleado():#Faltan validaciones
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
        

    def crearDepartamento(): #Faltan validaciones
        print(" >> Creacion de departamento <<")
        nombre = input("Ingrese nombre:\n> ")
        descripcion = input("Ingrese descripcion:\n> ")
        id_empleado = None
        question = input("Desea agregar un gerente a cargo? s/n\n> ")
    
        if question == "s":
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
        

    def editarDepartamento(self): #Faltan validaciones
        print(" >> Departamentos disponibles <<")
        departamentos = obtener_departamentos()
        for i in departamentos:
            print(DataFrame(i))
        print("\nIngrese el ID")
        id_departamento = input("> ")
        
        while True:
            depto = obtener_informacion_departamento(id_departamento)
            print(f" >> Departamento {depto["Nombre"]} <<")
            for key,item in depto.items():
                print(f"{key}: {item}")
            
            opciones = ["Gerente asignado","Nombre","Descripción","Estado","Salir"]
            print(" >> Edicion de departamento <<")
            print("Que desea modificar?")
            for i in enumerate(opciones):
                print(i)
            eleccion = input("> ")
            if eleccion == "1":
                print("Ingrese el ID del nuevo gerente")
                self.__id_empleado = input("> ")
                if departamento_editar_id_empleado(id_departamento,self.__id_empleado):
                    print("Edición completada con éxito!")
            elif eleccion == "2":
                print("Ingrese el nombre")
                self.__nombre = input("> ")
                if departamento_editar_nombre(id_departamento,self.__nombre):
                    print("Edición realizada con éxito!")
            elif eleccion == "3":
                print("Ingrese la descripción")
                self.__descripcion = input("> ")
                if departamento_editar_descripcion(id_departamento,self.__descripcion):
                    print("Edición realizada con éxito!")
            elif eleccion == "4":
                print("Ingrese el estado")
                print("1. Inactivo")
                print("2. Activo")
                estado = input("> ")
                if estado == "1":
                    self.__estado = "Inactivo"
                elif estado == "2":
                    self.__estado = "Activo"
                if departamento_editar_estado(id_departamento,self.__estado):
                    print("Edición realizada con éxito!")
            elif eleccion == "5":
                break
        
    
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