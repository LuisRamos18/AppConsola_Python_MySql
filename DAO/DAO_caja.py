#Importar de DAO la conexion a la base de datos
from DAO.DAO_conexion import DAO
from mysql.connector import Error

class FuncionesCaja:
    def __init__(self):
        self.dao = DAO()
#Método para leer todas las clientes en la BD
    def listarClientes(self):
        if self.dao.conexion.is_connected():
            try:
                cursor = self.dao.conexion.cursor()
                cursor.execute ("SELECT T0.ID_cliente, T0.Nombres, T0.Apellidos, T0.Direccion FROM clientes T0 LEFT JOIN bloqueados T1 ON T0.ID_cliente = T1.ID_cliente WHERE T1.ID_cliente IS NULL")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Eror al intentar la conexion:{0}",format(ex))

