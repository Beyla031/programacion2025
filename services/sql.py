def conectar(consulta_sql):
    #Módulo para conectar con base de datos SQL
    import mysql.connector
 

#Configuración de la conexión/ credenciales
    config = {
        'user': 'uayaxakc47tovhih',
        'password': '9yusDttY9F2uGNvnyxtE',
        'host': 'bsr9zztwkuuvg74hhhhl-mysql.services.clever-cloud.com',
        'database': 'bsr9zztwkuuvg74hhhhl',
        'raise_on_warnings': True
    }


# Conectar a la base de datos 
    try: 
       conexion = mysql.connector.connect(**config)
       print("Conexión exitosa a la base de datos.")

    #Objeto para crear consultas
       consultas = conexion.cursor()

       #Función para agregar la consulta SQL
       consultas.execute(consulta_sql)
       #Almacenamos el resultado de la consulta SQL
       resultado = consultas.fetchall()

       return resultado
     
    #Respuesta si al conectar da error 
    except mysql.connector.Error as err:
       print(f"Error al conectar a la base de datos: {err}")

