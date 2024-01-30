import pymysql

import pymysql

class EstudianteDB:
    def __init__(self):
        self.conexion = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='examen',
            port=3006,
            cursorclass=pymysql.cursors.DictCursor  # Asegúrate de agregar esta línea
        )


    
  
    def listar_estudiantes(self):
        with self.conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM Estudiante")
            estudiantes = cursor.fetchall()
        return estudiantes

    def agregar_estudiante(self, cedula, nombre, direccion, telefono):
        with self.conexion.cursor() as cursor:
            cursor.execute("INSERT INTO Estudiante (cedula, nombre, direccion, telefono) VALUES (%s, %s, %s, %s)", 
                           (cedula, nombre, direccion, telefono))
        self.conexion.commit()

    def obtener_estudiante(self, id):
        with self.conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM Estudiante WHERE id = %s", (id,))
            estudiante = cursor.fetchone()
        return estudiante

    def actualizar_estudiante(self, id, cedula, nombre, direccion, telefono):
        with self.conexion.cursor() as cursor:
            cursor.execute("UPDATE Estudiante SET cedula = %s, nombre = %s, direccion = %s, telefono = %s WHERE id = %s", 
                           (cedula, nombre, direccion, telefono, id))
        self.conexion.commit()

    def eliminar_estudiante(self, id):
        with self.conexion.cursor() as cursor:
            cursor.execute("DELETE FROM Estudiante WHERE id = %s", (id,))
        self.conexion.commit()
