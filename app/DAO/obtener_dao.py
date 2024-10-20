from app.DAO.DB import conexion

def obtener_id(rut):
    query = f"SELECT id_empleado FROM empleado WHERE rut = {rut}"
    try:
        conexion.get_cursor().execute(query)
        if id := conexion.fetchone():
            return id
    except Exception:
        pass
    return

def verificar_login(id,password):
    query = "select e.id_empleado,e.nombre,e.apellido_paterno, e.nivel_acceso, p.psw "
    query += "from empleado e "
    query += "join password p using(id_empleado) "
    query += f"WHERE `id_empleado` = {id}"
    try:
        conexion.get_cursor().execute(query)
        if usuario := conexion.fetchone():
            if usuario["psw"] == password:
                return {
                    "id_empleado": usuario["id_empleado"],
                    "nombre": usuario["nombre"],
                    "apellido_paterno": usuario["apellido_paterno"],
                    "nivel_acceso": usuario["nivel_acceso"]
                }
    except Exception as e:
        print(f"Error al loguear: {e}")
    return

def obtener_informacion_usuario(id_empleado):
    try:
        query = f"SELECT * FROM `empleado` WHERE id_empleado = {id_empleado}"
        conexion.get_cursor().execute(query)
        usuario = conexion.fetchall()
        if usuario:
            return usuario
    except Exception as e:
        print(f"Error al obtener la informacion: {e}")
    return

def obtener_departamentos():
    query = "SELECT `id_departamento`, `nombre` FROM `departamento`"
    try:
        conexion.get_cursor().execute(query)
        departamentos = conexion.fetchall()
        return departamentos
    except Exception as e:
        print(f"Error al obtener la informacion de los departamentos: {e}")
    return

def obtener_informacion_departamento(id_departamento):
    query = f"SELECT * FROM `departamento` WHERE id_departamento = {id_departamento}"
    try:
        conexion.get_cursor().execute(query)
        depto = conexion.fetchone()
        return {
            "ID": depto["id_departamento"],
            "Gerente": depto["id_empleado"],
            "Nombre": depto["nombre"],
            "Descripción": depto["descripcion"],
            "Estado": depto["estado"]
        }
    except Exception as e:
        print(f"Error al obtener la informacion del departamento: {e}")
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