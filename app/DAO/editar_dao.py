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