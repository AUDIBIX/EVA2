from app.DAO.DB import conexion
from app.DTO.Empleado import Empleado
from app.DTO.Departamento import Departamento

def ingresar_empleado(objeto_empleado:Empleado):
    query = "INSERT INTO `empleado`("
    query += "`nombre`,`apellido_paterno`,`apellido_materno`,"
    query += "`direccion`,`fono`,"
    query += "`salario`, `nivel_acceso`,"
    query += "`password`, `rut`, `id_departamento`, `email`)"
    
    query += f"VALUES ('{objeto_empleado.get_nombre()}','{objeto_empleado.get_apellido_paterno()}','{objeto_empleado.get_apellido_materno()}',"
    query += f"'{objeto_empleado.get_direccion()}','{objeto_empleado.get_numero_telefonico()}',"
    query += f"'{objeto_empleado.get_salario()}','{objeto_empleado.get_nivel_acceso()}',"
    query += f"'{objeto_empleado.get_password()}','{objeto_empleado.get_rut()}',Null,'{objeto_empleado.get_email()}')"
    
    try:
        conexion.get_cursor().execute(query)
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al ingresar el empleado: {e}")
        conexion.rollback()
    return False

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
    return False