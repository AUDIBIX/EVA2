from app.DAO.DB import conexion

def verificar_login(id,password):
    query = f"SELECT `id_empleado`, `nombre`, `apellido_paterno`, `nivel_acceso`, `password` FROM `empleado` WHERE `id_empleado` = {id}"
    try:
        conexion.get_cursor().execute(query)
        if usuario := conexion.fetchone():
            if usuario["password"] == password:
                return {
                    "id_empleado": usuario["id_empleado"],
                    "nombre": usuario["nombre"],
                    "apellido_paterno": usuario["apellido_paterno"],
                    "nivel_acceso": usuario["nivel_acceso"]
                }
    except Exception as e:
        print(f"Error al loguear: {e}")
    return False