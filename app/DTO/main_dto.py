from app.DAO.main_dao import verificar_login

def login():
    intentos = 3
    while intentos > 0:
        print("Ingrese ID de empleado:")
        usuario = input("> ")
        print("Ingrese contraseña:")
        contrasena = input("> ")
        if usuario := verificar_login(usuario,contrasena):
            return usuario
        intentos -= 1
        print("Usuario o contraseña incorrectos, intente nuevamente")