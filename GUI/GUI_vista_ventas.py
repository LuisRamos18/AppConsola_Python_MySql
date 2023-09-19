import GUI.GUI_menu as GUI_menu
import BO.BO_ventas as BO_ventas
from DAO.DAO_ventas import AccesoDatosVentas
import os
import time


#Vista para el módulo de ventas
def VistaVentas():
    print("Menú de Ventas")
    print("1.Vender")
    print("2.Cancelación")
    print("3.Lista de Ventas")
    print("4.Ir a menú principal")
#Validación para la seleccion, o regresar al menú principal
    seleccion = int(input("Ingresa una opción:"))
    if (seleccion < 1 or seleccion >4 ):
        print("Opción incorrecta, intenta de nuevo")
    elif seleccion == 4:
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
        acceso = AccesoDatosVentas()
        entrada = BO_ventas.RegistrarVenta()
        acceso.IngresarVenta(entrada)

    elif(seleccion == 2):
        time.sleep(2)
        os.system('cls')
        print("Módulo de cancelaciones")
        try:
            acceso = AccesoDatosVentas()
            ventas = acceso.listarVentas()
            if len(ventas) > 0:
                venta = BO_ventas.CancelarVenta(ventas)
                if venta:
                     acceso.ActualizarVenta(venta)
                else:
                    print("Folio de venta no ecnontrada..\n")
            else:
                print("Codigo de curso no encontrado....\n")
        except:
            print("Ocurrió un error")

    elif(seleccion == 3):
        time.sleep(2)
        os.system('cls')
        print("Listado de ventas")
        acceso = AccesoDatosVentas()
        ventas = acceso.listarVentas()
        if len(ventas) > 0:
            BO_ventas.listarVentas(ventas)
        else:
            print("No se encontraron cursos....")



 






    