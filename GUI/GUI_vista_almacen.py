import GUI.GUI_menu as GUI_menu
import BO.BO_almacen as BO_almacen
from DAO.DAO_almacen import FuncionesAlmacen
import os
import time


#Vista para el módulo de ventas
def VistaAlmacen():
    print("Menú de Almacén")
    print("1.Alta de producto")
    print("2.Entradas")
    print("3.Salidas")
    print("4.Existencias")
    print("5.Proveedores")
    print("6.Cancelaciones")
    print("7.Ir a menú principal")
#Validación para la seleccion, o regresar al menú principal
    seleccion = int(input("Ingresa una opción:"))
    if (seleccion < 1 or seleccion >7 ):
        print("Opción incorrecta, intenta de nuevo")
    elif seleccion == 7:
        time.sleep(1)
        os.system('cls')
        vista = GUI_menu.MenuPrincipal()
    else:
        EjecutarSubvista(seleccion)

#Método para llevar a cabo la opción seleccionada
def EjecutarSubvista(seleccion):
    if(seleccion == 1):
        time.sleep(2)
        os.system('cls')
        print("Módulo de venta")
        funcion = FuncionesAlmacen()
        entrada = BO_almacen.RegistrarProducto()
        funcion.IngresarProducto(entrada)
    elif(seleccion == 2):
        time.sleep(2)
        os.system('cls')
        print("Entrada")
        print("Módulo de venta")
        funcion = FuncionesAlmacen()
        entrada = BO_almacen.RegistrarEntrada()
        funcion.IngresarEntrada(entrada)
    elif(seleccion == 3):
        time.sleep(2)
        os.system('cls')
        print("Salidas")
        try:
            funcion = FuncionesAlmacen()
            inv = funcion.listarExistencia()
            if len(inv) > 0:
                inventario = BO_almacen.RegistarSalida(inv)
                if inventario:
                     funcion.IngresarSalida(inventario)
                else:
                    print("ID no encontrado..\n")
            else:
                print("Codigo de curso no encontrado....\n")
        except:
            print("Ocurrió un error")
    elif(seleccion == 4):
        time.sleep(2)
        os.system('cls')
        print("Listado de existencias")
        funcion = FuncionesAlmacen()
        exis = funcion.listarExistencia()
        if len(exis) > 0:
            BO_almacen.listarExistencias(exis)
        else:
            print("No se encontraron existencias....")