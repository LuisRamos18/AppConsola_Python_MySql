import GUI.GUI_menu as GUI_menu
import BO.BO_empleados as BO_empleados
from DAO.DAO_empleados import FuncionesEmpleados
import os
import time


#Vista para el módulo de ventas
def VistaEmpleados():
    print("Menú de Empleados")
    print("1.Dar de alta")
    print("2.Lista de empleados")
    print("3.Actualizar")
    print("4.Dar de baja")
    print("5.Ir a menú principal")
#Validación para la seleccion, o regresar al menú principal
    seleccion = int(input("Ingresa una opción:"))
    if (seleccion < 1 or seleccion >5 ):
        print("Opción incorrecta, intenta de nuevo")
    elif seleccion == 5:
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
        print("Alta de clientes")
        funcion = FuncionesEmpleados()
        entrada = BO_empleados.RegistrarEmpleado()
        funcion.IngresarEmpleado(entrada)

    elif(seleccion == 2):
        time.sleep(2)
        os.system('cls')
        print("Listado de clientes")
        funcion = FuncionesEmpleados()
        clientes = funcion.listarEmpleados()
        if len(clientes) > 0:
            BO_empleados.listarEmpleados(clientes)
        else:
            print("No se encontraron clientes....")

    elif(seleccion == 3):
        time.sleep(2)
        os.system('cls')
        print("Actualizacion de clientes")
        try:
            funcion = FuncionesEmpleados()
            clientes = funcion.listarEmpleados()
            if len(clientes) > 0:
                cliente = BO_empleados.PedirEmpleado(clientes)
                if cliente:
                     funcion.ActualizarEmpleado(cliente)
                else:
                    print("ID no encontrado..\n")
            else:
                print("Codigo de curso no encontrado....\n")
        except:
            print("Ocurrió un error")

    elif(seleccion == 4):
        time.sleep(2)
        os.system('cls')
        print("Bloqueo de clientes")
        try:
            funcion = FuncionesEmpleados()
            clientes = funcion.listarEmpleados()
            if len(clientes) > 0:
                cliente = BO_empleados.BloquearEmpleado(clientes)
                if cliente:
                     funcion.BloqueoEmpleado(cliente)
                else:
                    print("ID no encontrado..\n")
            else:
                print("No hay clientes para bloquear....\n")
        except:
            print("Ocurrió un error")