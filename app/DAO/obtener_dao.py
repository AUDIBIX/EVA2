from app.DAO.DB import conexion

def obtener_informacion_usuario(id_empleado):
    try:
        query = f"SELECT * FROM `empleado` WHERE id_empleado = {id_empleado}"
        conexion.get_cursor().execute(query)
        usuario = conexion.fetchall()
        if usuario:
            return {
                "Nombre": usuario["nombre"],
                "Apellido Paterno": usuario["apellido_paterno"],
                "Apellido Materno": usuario["apellido_materno"],
                "Rut": usuario["rut"],
                "Dirección": usuario["direccion"],
                "Fono": usuario["fono"],
                "Salario": usuario["salario"],
                "Nivel de acceso": usuario["nivel_acceso"],
                "Fecha de inicio del contrato": usuario["fecha_inicio_contrato"],
            }
    except Exception:
        pass
    return False

def obtener_departamentos():
    query = "SELECT `id_departamento`, `nombre` FROM `departamento`"
    try:
        conexion.get_cursor().execute(query)
        departamentos = conexion.fetchall()
        for depto in departamentos:
            {
                "ID": depto["id_departamento"],
                "Nombre": depto["nombre"]
            }
        return departamentos
    except Exception as e:
        print(f"Error al obtener la informacion de los departamentos: {e}")
    return False

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
    return False