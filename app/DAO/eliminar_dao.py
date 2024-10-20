from app.DAO.DB import conexion

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