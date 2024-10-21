from app.DAO.DB import conexion


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


def obtener_id(rut):
    query = f"SELECT id_empleado FROM empleado WHERE rut = {rut}"
    try:
        conexion.get_cursor().execute(query)
        if id := conexion.fetchone():
            return id
    except Exception:
        pass
    return


def obtener_un_empleado(id_empleado):
    try:
        query = f"SELECT * FROM empleado JOIN password using(id_empleado) WHERE id_empleado = {id_empleado}"
        conexion.get_cursor().execute(query)
        usuario = conexion.fetchone()
        if usuario:
            return usuario
    except Exception as e:
        print(f"Error al obtener la informacion del usuario: {e}")
    return

def obtener_empleados():
    query = "SELECT * FROM empleado"
    try:
        conexion.get_cursor().execute(query)
        if lista_empleados := conexion.fetchall():
            return lista_empleados
    except Exception as e:
        print(f"Error al recuperar empleados: {e}")
    return


def obtener_gerentes():
    query = "SELECT id_empleado,nombre,apellido_paterno FROM empleado WHERE nivel_acceso = 'gerente' AND (id_departamento IS NULL OR id_departamento = '')"
    try:
        conexion.get_cursor().execute(query)
        if gerentes := conexion.fetchall():
            return gerentes
    except Exception as e:
        print(f"Error al obtener lista de gerentes disponibles: {e}")
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


def eliminar_usuario(id):
    query = f"DELETE FROM empleado WHERE id_empleado = {id}"
    try:
        conexion.get_cursor().execute(query)
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al eliminar empleado: {e}")
        conexion.rollback()
    return