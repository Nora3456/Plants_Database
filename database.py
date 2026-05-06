import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='plant_db',
            user='root',
            password='rootpassword'
        )
        return connection
    except Error as e:
        print("Error:", e)
        return None


def add_plant(connection, name):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO plants (name, type_id, size_id, location_id, sunlight_id) VALUES (%s, 1, 1, 1, 1)"
        cursor.execute(query, (name,))
        connection.commit()
        print("Plant added.")
    except Error as e:
        print("Error:", e)


def view_plants(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM plants")
    for row in cursor.fetchall():
        print(row)