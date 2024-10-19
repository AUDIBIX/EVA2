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
    
    def __str__(self):
        txt = f"Nombre completo: {self.__nombre} {self.__apellido_paterno} {self.__apellido_materno}\n"
        txt += f"Dirección: {self.__direccion}\n"
        txt += f"Número de teléfono: {self.__numero_telefonico}\n"
        txt += f"Correo electrónico: {self.__email}\n"
        txt += f"Fecha de inicio del contrato: {self.__fecha_inicio_contrato}\n"
        txt += f"Salario: {self.__salario}\n"
        txt += f"Nivel de acceso: {self.__nivel_acceso}\n"
        return txt