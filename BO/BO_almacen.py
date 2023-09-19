def RegistrarProducto():
    entradacodigo = False
    while(not entradacodigo):
        nombre = input("Ingresa la descripcion del producto:")
        unidad = input("Ingresa la unidad:")
        precio = input("Ingresa el precio:")
        if (precio.isalpha()):
            print("El precio tiene que ser numérico")
        else:
            entradacodigo = True
            producto = (nombre,unidad,precio)
            return producto
        
def RegistrarEntrada():
    entradacodigo = False
    while(not entradacodigo):
        producto= input("Ingresa el código del producto:")
        cantidad = input("Ingresa la cantidad:")
        tipo = 1
        if (cantidad.isalpha()):
            print("La cantidad tiene que ser numérico")
        else:
            entradacodigo = True
            entradas = (producto,cantidad,tipo)
            return entradas
        
#método para listar las ventas
def listarExistencias(existencia):
    print("Existencias:")
    contador =1 
    for ext in existencia:
        datos ="Codigo:{1}| Producto:{2} | Volumen:{3} | Unidad: {4})"
        print(datos.format(contador, ext[0], ext[1], ext[2], ext[3]))
        contador = contador+1

#Método para generar salidad
def RegistarSalida(salida):
    listarExistencias(salida)
    existeid= False
    idsacar = int(input("Ingrese el código del producto: "))
    cantidad = int(input("Ingrese la cantidad: "))
    tipo = 2
    for sl in salida:
        if sl[0] == idsacar:
            if sl[2] <= cantidad:
                existeid = True
            else:
                print("la salida no puede ser mayor a la existencia")
        else:
            break
    if existeid:
        datos = (idsacar,cantidad,tipo)
    else:
        datos = None
    return datos