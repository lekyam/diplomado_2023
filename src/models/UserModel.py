from src.database.database import get_connection
from entities.User import User


class UserModel():

    @classmethod
    def get_users(self):
        try:
            connection = get_connection()
            users = []
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento FROM usuario ORDER BY nombre ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    user = User(row[0], row[1], row[2], row[3], row[4])
                    users.append(user.to_JSON())
            connection.close()
            return users
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user(self, user_id):
        try:
            connection = get_connection()
            user = None
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento FROM usuario WHERE cedula_identidad = %s", (user_id,))
                row = cursor.fetchone()

                if row != None:
                    user = User(row[0], row[1], row[2], row[3], row[4])
                    user = user.to_JSON()
            connection.close()
            return user
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def create_user(self, user):
        try:
            connection = get_connection()
            affected_rows = None
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO usuario (cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento) VALUES  (%s, %s, %s, %s, %s)", (user.cedula_identidad, user.nombre, user.primer_apellido, user.segundo_apellido, user.fecha_nacimiento))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_user(self, user_cedula_identidad):
        try:
            connection = get_connection()
            affected_rows = None
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM usuario WHERE cedula_identidad = %s", (user_cedula_identidad,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_user(self, user):
        try:
            connection = get_connection()
            affected_rows = None
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE usuario SET nombre = %s, primer_apellido = %s, segundo_apellido = %s, fecha_nacimiento = %s WHERE cedula_identidad = %s", (user.nombre, user.primer_apellido, user.segundo_apellido, user.fecha_nacimiento, user.cedula_identidad))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_average_age(self):
        try:
            connection = get_connection()
            average_age = None
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT AVG(EXTRACT(YEAR FROM AGE(NOW(), fecha_nacimiento))) AS promedio_edades FROM usuario ")
                row = cursor.fetchone()
                if row != None:
                    average_age = {'promedioEdad': row[0]}
            connection.close()
            return average_age
        except Exception as ex:
            raise Exception(ex)
