from app.DAO.DB import conexion
from app.DTO.Departamento import Departamento


def ingresar_departamento(objeto_depto:Departamento):
    query = "INSERT INTO `departamento`("
    query += f"`id_empleado`, `nombre`, `descripcion`, `estado`) "
    query += f"VALUES ('{objeto_depto.get_id_gerente()}','{objeto_depto.get_nombre()}','{objeto_depto.get_descripcion()}','{objeto_depto.get_estado()}')"
    try:
        conexion.get_cursor().execute(query)
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al crear el departamento: {e}")
        conexion.rollback()
    return


def obtener_departamentos():
    query = "SELECT * FROM departamento"
    try:
        conexion.get_cursor().execute(query)
        departamentos = conexion.fetchall()
        return departamentos
    except Exception as e:
        print(f"Error al obtener la informacion de los departamentos: {e}")
    return


def obtener_un_departamento(id_departamento):
    query = f"SELECT * FROM `departamento` WHERE id_departamento = {id_departamento}"
    try:
        conexion.get_cursor().execute(query)
        depto = conexion.fetchone()
        return {
            "ID": depto["id_departamento"],
            "Gerente": depto["id_gerente"],
            "Nombre": depto["nombre"],
            "Descripción": depto["descripcion"],
            "Estado": depto["estado"]
        }
    except Exception as e:
        print(f"Error al obtener la informacion del departamento: {e}")
    return


def editar_departamento(id_departamento,atributo,nuevo_valor):
    query = f"UPDATE departamento SET {atributo} = {nuevo_valor} where id_departamento = {id_departamento}"
    try:
        conexion.get_cursor().execute(query)
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al modificar el departamento: {e}")
    return