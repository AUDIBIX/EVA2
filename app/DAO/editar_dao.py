from app.DAO.DB import conexion


def departamento_editar_id_empleado(id_departamento,id_empleado):
    query1 = "update departamento set id_empleado = %s where id_departamento = %s"
    query2 = "update empleado set id_departamento = %s where id_empleado = %s"
    try:
        conexion.get_cursor().execute(query1,(id_empleado,id_departamento,))
        conexion.get_cursor().execute(query2,(id_departamento,id_empleado,))
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error, la edicion no se pudo llevar a cabo: {e}")
        conexion.rollback()
    return False
    
def departamento_editar_nombre(id_departamento,nombre):
    query = "update departamento set nombre = %s where id_departamento = %s"
    try:
        conexion.get_cursor().execute(query,(nombre,id_departamento,))
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error, la edicion no se pudo llevar a cabo: {e}")
    return False

def departamento_editar_descripcion(id_departamento,descripcion):
    query = "update departamento set descripcion = %s where id_departamento = %s"
    try:
        conexion.get_cursor().execute(query,(descripcion,id_departamento,))
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error, la edicion no se pudo llevar a cabo: {e}")
    return False
    
def departamento_editar_estado(id_departamento,estado):
    query = "update departamento set estado = %s where id_departamento = %s"
    try:
        conexion.get_cursor().execute(query,(estado,id_departamento,))
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error, la edicion no se pudo llevar a cabo: {e}")
    return False