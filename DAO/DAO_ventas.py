#Importar de DAO la conexion a la base de datos
from DAO.DAO_conexion import DAO
from mysql.connector import Error

class AccesoDatosVentas:
    def __init__(self):
        self.dao = DAO()
#Instancias
#Método para leer todas las ventas en la BD
    def listarVentas(self):
        if self.dao.conexion.is_connected():
            try:
                cursor = self.dao.conexion.cursor()
                cursor.execute ("Select T0.Folio,T1.Producto,T0.Pago,T0.Cambio from ventas T0 INNER JOIN productos T1 on T0.Codigo = T1.Codigo WHERE T0.Estado = 1")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Eror al intentar la conexion:{0}",format(ex))

#Método para insertar ventas en la BD    
    def IngresarVenta(self, producto):
        if self.dao.conexion.is_connected():
            try:
                cursor = self.dao.conexion.cursor()
                sql = "Insert into ventas (ID_cliente,Codigo,Pago) values ({0},{1},{2})"
                cursor.execute(sql.format(producto[0],producto[1],producto[2]))
                self.dao.conexion.commit()
                print("Venta realizada\n")
            except Error as ex:
                print("Eror al intentar la conexion:{0}",format(ex))

#Método para cancelar la venta en la BD (Actualiza el estado)
    def ActualizarVenta(self, cancelar):
        if self.dao.conexion.is_connected():
            try:
                cursor = self.dao.conexion.cursor()
                sql = "UPDATE ventas set Estado = {0}, Motivo = '{1}' where Folio = {2}"
                cursor.execute(sql.format(cancelar[1],cancelar[2],cancelar[0]))
                self.dao.conexion.commit()
                print("Venta cancelada\n")
            except Error as ex:
                print("Eror al intentar la conexion:{0}",format(ex))




