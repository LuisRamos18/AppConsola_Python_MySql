#Importar de DAO la conexion a la base de datos
from DAO.DAO_conexion import DAO
from mysql.connector import Error

class FuncionesEmpleados:
    def __init__(self):
        self.dao = DAO()
#Método para leer todas las clientes en la BD
    def listarEmpleados(self):
        if self.dao.conexion.is_connected():
            try:
                cursor = self.dao.conexion.cursor()
                cursor.execute ("SELECT T0.ID_empelado, T0.Nombres,T0.Apellidos,T1.nombre_puesto ,T2.departamento FROM empleados T0 INNER JOIN puestos T1 ON T0.Puesto = T1.ID_puesto INNER JOIN departamentos T2 ON T1.departamento = T2.ID_departamento")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Eror al intentar la conexion:{0}",format(ex))

#Método para insertar clientes en la BD    
    def IngresarEmpleado(self, clientes):
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
    def ActualizarEmpleado(self, datos):
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
    def BloqueoEmpleado(self, datos):
        if self.dao.conexion.is_connected():
            try:
                cursor = self.dao.conexion.cursor()
                sql = "Insert into bloqueados (ID_cliente, Motivo) values ({0},'{1}')"
                cursor.execute(sql.format(datos[0],datos[1]))
                self.dao.conexion.commit()
                print("Bloqueo exitoso!\n")
            except Error as ex:
                print("Eror al intentar la conexion:{0}",format(ex))