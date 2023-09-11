datos = {
    "usuario": {"nombre_user": "usuario", "password": "usuario"},
    "administrador": {"nombre_user": "administrador", "password": "administrador_123"},
    "superusuario": {"nombre_user": "Cristian", "password": "Cristian_123"}
}

def verificar_aut(usuario):
    def decorador(func):
        def funcion_aut(*args, **kwargs):
            if "nombre_user" in kwargs and "password" in kwargs:
                if (kwargs["nombre_user"] == datos[usuario]["nombre_user"] and
                        kwargs["password"] == datos[usuario]["password"]):
                    return func()
                else:
                    return "Acceso denegado para", usuario
            else:
                return "Se requieren credenciales."
        return funcion_aut
    return decorador

# Funciones para cada autenticacion.
@verificar_aut("usuario")
def funcion_usuario():
    return "Función de usuario normal."

@verificar_aut("administrador")
def funcion_administrador():
    return "Función de administrador."

@verificar_aut("superusuario")
def funcion_superusuario():
    return "Función de superusuario."

print(funcion_usuario(nombre_user="usuario", password="usuario"))
print(funcion_administrador(nombre_user="administrador", password="administrador_123"))
print(funcion_superusuario(nombre_user="Cristian", password="Cristian_123"))