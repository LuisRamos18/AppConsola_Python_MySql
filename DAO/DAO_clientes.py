#Importar de DAO la conexion a la base de datos
from DAO.DAO_conexion import DAO
from mysql.connector import Error

class FuncionesClientes:
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

#Método para insertar clientes en la BD    
    def IngresarCliente(self, clientes):
        if self.dao.conexion.is_connected():
            try:
                cursor = self.dao.conexion.cursor()
                sql = "Insert into clientes (Nombres, Apellidos, Direccion) values ('{0}','{1}','{2}')"
                cursor.execute(sql.format(clientes[0],clientes[1],clientes[2]))
                self.dao.conexion.commit()
                print("Alta exitosa!\n")
            except Error as ex:
                print("Eror al intentar la conexion:{0}",format(ex))


#Método para actualizar los datos del cliente
    def ActualizarCliente(self, datos):
        if self.dao.conexion.is_connected():
            try:
                cursor = self.dao.conexion.cursor()
                sql = "UPDATE clientes set Nombres = '{0}', Apellidos = '{1}', Direccion = '{2}' where ID_cliente= {3}"
                cursor.execute(sql.format(datos[1],datos[2],datos[3],datos[0]))
                self.dao.conexion.commit()
                print("Actualización exitosa!\n")
            except Error as ex:
                print("Eror al intentar la conexion:{0}",format(ex))

#Método para bloquear clientes
    def BloqueoCliente(self, datos):
        if self.dao.conexion.is_connected():
            try:
                cursor = self.dao.conexion.cursor()
                sql = "Insert into bloqueados (ID_cliente, Motivo) values ({0},'{1}')"
                cursor.execute(sql.format(datos[0],datos[1]))
                self.dao.conexion.commit()
                print("Bloqueo exitoso!\n")
            except Error as ex:
                print("Eror al intentar la conexion:{0}",format(ex))
