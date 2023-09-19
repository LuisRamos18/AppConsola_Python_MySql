#Importar de DAO la conexion a la base de datos
from DAO.DAO_conexion import DAO
from mysql.connector import Error

class FuncionesAlmacen:
    def __init__(self):
        self.dao = DAO()
        
    def IngresarProducto(self, producto):
        if self.dao.conexion.is_connected():
            try:
                cursor = self.dao.conexion.cursor()
                sql = "Insert into productos (Producto,Unidad, Precio) values ('{0}','{1}',{2})"
                cursor.execute(sql.format(producto[0],producto[1],producto[2]))
                self.dao.conexion.commit()
                print("Producto Registrado\n")
            except Error as ex:
                print("Eror al intentar la conexion:{0}",format(ex))


    def IngresarEntrada(self, entradas):
        if self.dao.conexion.is_connected():
            try:
                cursor = self.dao.conexion.cursor()
                sql = "Insert into movimientos (ID_producto,Cantidad,Tipo_Mov) values ({0},{1},{2})"
                cursor.execute(sql.format(entradas[0],entradas[1],entradas[2]))
                self.dao.conexion.commit()
                print("Entrada exitosa\n")
            except Error as ex:
                print("Eror al intentar la conexion:{0}",format(ex))

#Método para leer todas las existencias
    def listarExistencia(self):
        if self.dao.conexion.is_connected():
            try:
                cursor = self.dao.conexion.cursor()
                cursor.execute ("WITH EN AS(SELECT ID_producto, SUM(Cantidad)AS 'Entradas' FROM `movimientos` WHERE Tipo_Mov =1 GROUP BY ID_producto), SA AS(SELECT ID_producto, SUM(Cantidad)AS 'Salidas' FROM `movimientos` WHERE Tipo_Mov =2 GROUP BY ID_producto) SELECT EN.ID_producto, P.Producto, CASE WHEN SA.Salidas IS NULL AND SA.ID_producto IS NULL THEN EN.Entradas ELSE EN.Entradas - SA.Salidas END AS Final,P.Unidad FROM EN LEFT JOIN SA ON EN.ID_producto = SA.ID_producto INNER JOIN productos P ON P.Codigo = EN.ID_producto")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Eror al intentar la conexion:{0}",format(ex))

#Método generar una salidad del almacén
    def IngresarSalida(self, datos):
        if self.dao.conexion.is_connected():
            try:
                cursor = self.dao.conexion.cursor()
                sql = "Insert into movimientos (ID_producto,Cantidad,Tipo_Mov) values ({0},{1},{2})"
                cursor.execute(sql.format(datos[0],datos[1],datos[2]))
                self.dao.conexion.commit()
                print("Salida exitosa\n")
            except Error as ex:
                print("Eror al intentar la conexion:{0}",format(ex))
 