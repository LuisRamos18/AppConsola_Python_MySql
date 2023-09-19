import GUI.GUI_vista_ventas as vistas_ventas
import GUI.GUI_vista_almacen as vistas_almacen
import GUI.GUI_vista_clientes as vistas_cliente
import GUI.GUI_vista_empleados as vistas_empleado
import GUI.GUI_vista_caja as vistas_caja
import datetime
import time
import os

#Variable para almacenar fecha y hora actual
fecha_hora_actual = datetime.datetime.now()


def MenuPrincipal():
    continuar = True
    while(continuar):
        print("Bienvenido al menú principal, selecciona una opción")
        print (fecha_hora_actual)
        print("1.Ventas\n")
        print("2.Almacén\n")
        print("3.Clientes\n")
        print("4.Empleados\n")
        print("5.Caja\n")
        print("6.Salir\n")
        opcion = int(input("Ingresa una opción:"))
        if (opcion < 1 or opcion >6 ):
            print("Opción incorrecta, intenta de nuevo")
        elif opcion == 5:
            continuar = False
            print("Gracias por usar el sistema!")
            break
        else:
            EjecutarOpcion(opcion)

#Metodo para acceder a las vistas por opcion
def EjecutarOpcion(opcion):
    if(opcion == 1):
        time.sleep(2)
        os.system('cls')
        vista = vistas_ventas.VistaVentas()
    elif (opcion == 2):
        time.sleep(2)
        os.system('cls')
        vista = vistas_almacen.VistaAlmacen()
    elif (opcion == 3):
        time.sleep(2)
        os.system('cls')
        vista = vistas_cliente.VistaClientes()
    elif (opcion == 4):
        time.sleep(2)
        os.system('cls')
        vista = vistas_empleado.VistaEmpleados()
    elif (opcion == 5):
        time.sleep(2)
        os.system('cls')
        vista = vistas_caja.VistaCaja()
  