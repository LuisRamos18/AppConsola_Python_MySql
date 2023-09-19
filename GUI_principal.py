from DAO.DAO_login import ValidadorDeLogin
import BO.BO_login as login
import GUI.GUI_menu as GUI_menu
import time
import os

# Validación de datos de inicio
print(" *****************************")
print("******** Inicio de Sesión ********")
print(" *****************************\n")
dao = ValidadorDeLogin()
while True:
#Lllamar al método para el ingreso de los datos
    entrada = login.PedirDatos()
    if dao.ValidarDatos(entrada):
        usuario = (format(entrada[0]))
        print("¡Inicio de sesión exitoso! Bienvenido",usuario)
        time.sleep(2)
        os.system('cls')
        vista = GUI_menu.MenuPrincipal()
        break
    else:
        print("Usuario y/o clave incorrecta, intenta de nuevo")


