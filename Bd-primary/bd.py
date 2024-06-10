# bd.py
import mysql.connector

def conectar():
    try: 
        conexion = mysql.connector.connect(user= 'root', password= 'DYKIvAjxdkZzajLNkRcKHQPPnxzwyoKt', 
                                   host= 'monorail.proxy.rlwy.net', 
                                   database='railway',
                                   port='10919')
        print("Conexión realizada")
        return conexion
    except mysql.connector.Error as Err:
        return 'Error al registrar usuario'
#Hola