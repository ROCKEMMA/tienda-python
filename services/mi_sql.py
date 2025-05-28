import mysql.connector

def conectar(consulta_sql):

    # Credenciales para la conexión
    config = {
        'user': 'uzxqz8kn5gkz5jrl',
        'password': 'rMcwd3w8aVzkxkhA8Gu5',
        'host': 'biikh2v3gnklg76bq5xd-mysql.services.clever-cloud.com',
        'database': 'biikh2v3gnklg76bq5xd',
        'raise_on_warnings': True
    }

    # Conectar a la base de datos
    try:
        conexion = mysql.connector.connect(**config)
        print("Conexión exitosa a la base de datos.")

        # Objeto para crear consultas
        consulta = conexion.cursor()

        # función para agregar la consulta SQL
        consulta.execute(consulta_sql)

        # Almacenamos el resultado de la consulta SLQ
        resultado = consulta.fetchall()

        return resultado

    # Respuesta si al conectar da error
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")