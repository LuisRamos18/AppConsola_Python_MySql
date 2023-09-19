#Importar de DAO la conexion a la base de datos
from DAO.DAO_conexion import DAO
from mysql.connector import Error

class ValidadorDeLogin:
    def __init__(self):
        self.dao = DAO()

    def ValidarDatos(self, inicio):
        if self.dao.conexion.is_connected():
            try:
                cursor = self.dao.conexion.cursor()
                sql = "SELECT * FROM usuarios WHERE usuario = '{0}' AND clave = '{1}'"
                cursor.execute(sql.format(inicio[0], inicio[1]))
                resultado = cursor.fetchone()
                if resultado is not None:
                    return True
                else:
                    return False
            except Error as ex:
                print("Error al intentar la conexion", ex)