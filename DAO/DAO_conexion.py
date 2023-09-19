#importar las librerias para la conexion a la base de datos mysql
import mysql.connector
from mysql.connector import Error


#Crear la clase para la conexion
class DAO:
    def __init__(self):
        #estructura de control para manejo de excepciones
        try:
            self.conexion = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "proyecto1"
            )
        except Error as ex:
            print("Error al intentar la conexion",ex)


