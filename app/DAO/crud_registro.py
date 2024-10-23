from app.DAO.DB import conexion
from app.DTO.Registro_de_tiempo import Registro_de_tiempo as Registro

def crearRegistro(registro:Registro):
    query = f"INSERT INTO `registro_de_tiempo`"
    query += f"(`id_empleado`, `fecha_registro`, `descripcion`, `cantidad_horas`) "
    query += f"VALUES ('{registro.get_id_empleado()}','{registro.get_fecha_registro()}','{registro.get_descripcion()}','{registro.get_cantidad_horas()}')"
    try:
        conexion.get_cursor().execute(query)
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al agregar registro de tiempo: {e}")
        conexion.rollback()
        return
    
def obtenerRegistros():
    query = "SELECT * FROM registro_de_tiempo"
    try:
        conexion.get_cursor().execute(query)
        return conexion.fetchall()
    except Exception as e:
        print(f"Error al obtener el registro: {e}")
    return

def obtener_un_registro(id):
    query = f"SELECT * FROM registro_de_tiempo WHERE id_registro = {id}"
    try:
        conexion.get_cursor().execute(query)
        return conexion.fetchone()
    except Exception as e:
        print(f"Error al obtener el registro: {e}")
    return

def editarRegistro(id_registro,atributo,nuevo_valor):
    query = f"UPDATE registro_de_tiempo SET {atributo} = {nuevo_valor} WHERE id_registro = {id_registro}"
    try:
        conexion.get_cursor().execute(query)
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al actualizar registro: {e}")
        conexion.rollback()
    return

def eliminarRegistro(id):
    query = f"DELETE FROM registro_de_tiempo WHERE id_registro = {id}"
    try:
        conexion.get_cursor().execute(query)
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al eliminar registro: {e}")
        conexion.rollback()