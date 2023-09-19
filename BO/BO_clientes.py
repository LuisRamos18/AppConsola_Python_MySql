#método para listar las ventas
def listarClientes(clientes):
    print("Clientes:")
    contador =1 
    for cte in clientes:
        datos ="ID:{1}| Nombres:{2} | Apellidos:{3} | Dirección: {4})"
        print(datos.format(contador, cte[0], cte[1], cte[2], cte[3]))
        contador = contador+1
    print(" ")

#método para pedir los datos antes de ingresar
def RegistrarCliente():
    entradacte = False
    while(not entradacte):
        nombres = input("Ingresa los nombres:")
        apellidos= input("Ingresa los apellidos:")
        direccion = input("Ingresa los dirección:")
        if (nombres.isnumeric()):
            print("El nombre no pueder ser un número")
        else:
            entradacte = True
            cliente = (nombres,apellidos,direccion)
            return cliente
        
#Método para pedir el folio para luego Actualizar
def PedirCliente(cliente):
    listarClientes(cliente)
    existeid= False
    idactualizar = int(input("Ingrese el ID a actualizar: "))
    for cte in cliente:
        if cte[0] == idactualizar:
            existeid = True
            break
    if existeid:
        nombres = input("Ingresa los nombres:")
        apellidos = input("Ingresa los apellidos:")
        direccion = input("Ingresa la direccion:")
        datos = (idactualizar,nombres,apellidos,direccion)
    else:
        datos = None
    return datos

#Método para pedir el folio para luego Bloquear
def BloquearCliente(cliente):
    listarClientes(cliente)
    existeid= False
    idbloquear = int(input("Ingrese el ID a bloquear: "))
    for cte in cliente:
        if cte[0] == idbloquear:
            existeid = True
            break
    if existeid:
        motivo = input("Ingresa el motivo del bloqueo:")
        datos = (idbloquear,motivo)
    else:
        datos = None
    return datos