import mysql.connector

def conectar(consulta_sql):
    config = {
        'user': 'uayaxakc47tovhih',
        'password': '9yusDttY9F2uGNvnyxtE',
        'host': 'bsr9zztwkuuvg74hhhhl-mysql.services.clever-cloud.com',
        'database': 'bsr9zztwkuuvg74hhhhl',
        'raise_on_warnings': True
    }

    try:
        conexion = mysql.connector.connect(**config)
        print("Conexión exitosa a la base de datos.")
        consultas = conexion.cursor()
        consultas.execute(consulta_sql)
        resultado = consultas.fetchall()
        conexion.close()
        return resultado
    
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return []