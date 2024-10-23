from app.DAO.crud_empleados import obtener_un_empleado


def verificar_login(id,password):
    if usuario := obtener_un_empleado(id):
        if usuario["psw"] == password:
            return usuario
    return

def print_opciones(opciones=list):
    for idx,opcion in enumerate(opciones,start=1):
        print(f"{idx}. {opcion}")