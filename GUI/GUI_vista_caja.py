import GUI.GUI_menu as GUI_menu
import BO.BO_caja as BO_caja
from DAO.DAO_caja import FuncionesCaja
import os
import time


#Vista para el módulo de ventas
def VistaCaja():
    print("Menú de Caja")
    print("1.Apertura de caja")
    print("2.Arqueo de caja")
    print("3.Cierre de caja")
    print("4.Ir a menú principal")
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
        