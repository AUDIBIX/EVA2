from app.DAO.DB import conexion
from app.DAO.crud_empleados import obtener_un_empleado


def verificar_login(id,password):
    if usuario := obtener_un_empleado(id):
        if usuario["psw"] == password:
            return usuario
    return