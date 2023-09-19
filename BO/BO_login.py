def PedirDatos():
    entradausuario = False
    while(not entradausuario):
        usuario = input("Ingresa tu usuario:")
        if (usuario.isnumeric()):
            print("El usuario no pueden ser numeros")
        else:
            entradausuario = True
            clave = input("Ingresa tu clave:")
            inicio = (usuario, clave)
            return inicio