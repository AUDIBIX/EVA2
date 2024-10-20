from app.DAO.DB import conexion
from app.DTO.Empleado import Empleado
from app.DTO.Departamento import Departamento
from app.DAO.obtener_dao import obtener_id

def ingresar_credenciales_empleado(rut,psw):
    id = obtener_id(rut)
    query = f"INSERT INTO password(id_empleado,psw) values({id["id_empleado"]},{psw})"
    try:
        conexion.get_cursor().execute(query)
        return True
    except Exception as e:
        print(f"Error al ingresar empleado: {e}")
        conexion.rollback()
        return False

def ingresar_empleado(nombre,apellido_paterno,apellido_materno,direccion,fono,salario,nivel_acceso,rut,email,psw):
    query = "INSERT INTO `empleado`("
    query += "`nombre`,`apellido_paterno`,`apellido_materno`,"
    query += "`direccion`,`fono`,"
    query += "`salario`, `nivel_acceso`,"
    query += "`rut`, `email`)"
    
    query += f"VALUES ('{nombre}','{apellido_paterno}','{apellido_materno}',"
    query += f"'{direccion}','{fono}',"
    query += f"'{salario}','{nivel_acceso}',"
    query += f"'{rut}','{email}')"
    
    try:
        conexion.get_cursor().execute(query)
        if ingresar_credenciales_empleado(rut,psw):
            conexion.commit()
            return True
        else:
            conexion.rollback()
    except Exception as e:
        print(f"Error al ingresar empleado: {e}")
        conexion.rollback()
    return

def ingresar_departamento(objeto_depto:Departamento):
    query = "INSERT INTO `departamento`("
    query += f"`id_empleado`, `nombre`, `descripcion`, `estado`) "
    query += f"VALUES ('{objeto_depto.get_id_gerente()}','{objeto_depto.get_nombre()}','{objeto_depto.get_descripcion()}','{objeto_depto.get_estado()}')"
    try:
        conexion.get_cursor().execute(query)
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al crear el departamento: {e}")
        conexion.rollback()
    return