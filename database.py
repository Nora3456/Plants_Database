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


def add_plant(connection):
    try:
        cursor = connection.cursor()

        print("\n🌱 ADD NEW PLANT")
        print("=" * 30)

        # ---- BASIC INFO ----
        name = input("Plant name: ").strip()
        age = input("Age (e.g. 2 years, 5+ years): ").strip()

        # ---- SELECT TYPE ----
        print("\nSelect Plant Type:")
        cursor.execute("SELECT type_id, type_name FROM plant_types")
        types = cursor.fetchall()
        for t in types:
            print(f"{t[0]}. {t[1]}")
        type_id = int(input("Type ID: "))

        # ---- SELECT SIZE ----
        print("\nSelect Size:")
        cursor.execute("SELECT size_id, size_name FROM sizes")
        sizes = cursor.fetchall()
        for s in sizes:
            print(f"{s[0]}. {s[1]}")
        size_id = int(input("Size ID: "))

        # ---- SELECT LOCATION ----
        print("\nSelect Location:")
        cursor.execute("SELECT location_id, location_name FROM locations")
        locations = cursor.fetchall()
        for l in locations:
            print(f"{l[0]}. {l[1]}")
        location_id = int(input("Location ID: "))

        # ---- SELECT SUNLIGHT ----
        print("\nSelect Sunlight Level:")
        cursor.execute("SELECT sunlight_id, level FROM sunlight_levels")
        sunlight = cursor.fetchall()
        for s in sunlight:
            print(f"{s[0]}. {s[1]}")
        sunlight_id = int(input("Sunlight ID: "))

        # ---- INSERT PLANT ----
        query = """
            INSERT INTO plants (name, age, type_id, size_id, location_id, sunlight_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (name, age, type_id, size_id, location_id, sunlight_id)

        cursor.execute(query, values)
        connection.commit()

        print("\n✅ Plant added successfully!")

    except Exception as e:
        print(f"\n❌ Error adding plant: {e}")


def view_plants(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM plants")
    for row in cursor.fetchall():
        print(row)