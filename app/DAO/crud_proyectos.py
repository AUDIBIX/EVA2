from app.DAO.DB import conexion
from app.DTO.Proyecto import Proyecto

def ingresar_proyecto(objeto_proyecto:Proyecto):
    query = "INSERT INTO 'proyecto'("
    query += f"'id_departamento', 'nombre', 'descripcion', 'estado') "
    query += f"VALUES ('{objeto_proyecto.get_id_departamento()}','{objeto_proyecto.get_nombre()}',{objeto_proyecto.get_descripcion()},{objeto_proyecto.get_estado()})"
    try:
        conexion.get_cursor().execute(query)
        conexion.commit
        return True
    except Exception as e:
        print(f"Error al crear el Proyecto: {e}")
        conexion.rollback
    
    