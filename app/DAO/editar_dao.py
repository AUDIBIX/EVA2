from app.DAO.DB import conexion

def editar_departamento(id_departamento,atributo,nuevo_valor):
    query = f"UPDATE departamento SET {atributo} = {nuevo_valor} where id_departamento = {id_departamento}"
    try:
        conexion.get_cursor().execute(query)
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al modificar el departamento: {e}")
    return

def editar_usuario(id_empleado,atributo,nuevo_valor):
    query = f"UPDATE empleado SET {atributo} = {nuevo_valor} where id_empleado = {id_empleado}"
    try:
        conexion.get_cursor().execute(query)
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al modificar el usuario: {e}")
    return

def editar_psw(id_empleado,psw):
    query = "update password set psw = %s where id_empleado = %s"
    try:
        conexion.get_cursor().execute(query,(psw,id_empleado,))
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error, la edicion no se pudo llevar a cabo: {e}")
    return False