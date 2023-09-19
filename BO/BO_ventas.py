import BO.BO_clientes as BO_clientes
from DAO.DAO_clientes import FuncionesClientes

#método para listar las ventas
def listarVentas(ventas):
    print("Ventas:")
    contador =1 
    for ven in ventas:
        datos ="Folio:{1}| Producto:{2} | Pago:{3} | Cambio: {4})"
        print(datos.format(contador, ven[0], ven[1], ven[2], ven[3]))
        contador = contador+1
    print(" ")

#método para pedir los datos antes de ingresar
def RegistrarVenta():
    entradacodigo = False
    while(not entradacodigo):
        cte = input("Ingresa el número de cliente:")
        if (cte.isalpha()):
            print("El código de cliente es numérico")
        else:
            codigo = input("Ingresa el código del producto:")
            if (codigo.isalpha()):
                print("El código de producto es numérico")
            else:
                pago = input("Ingresa el pago:")
                if (codigo.isalpha()):
                    print("El pago debe ser unvalor numérico")
                else:
                    entradacodigo = True
                    producto = (cte,codigo,pago)
                    return producto



#Método para pedir el folio para luego cancelar (actualiza el estado)
def CancelarVenta(ventas):
    listarVentas(ventas)
    existefolio = False
    foliocancelar = int(input("Ingrese el Folio a cancelar: "))
    for ven in ventas:
        if ven[0] == foliocancelar:
            existefolio = True
            break
    if existefolio:
        estado = 2
        motivo = input("Ingresa el motivo de la cancelación:")
        cancelar = (foliocancelar,estado,motivo)
    else:
        cancelar = None
    return cancelar