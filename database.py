import mysql.connector
from mysql.connector import Error


def create_connection():
    """Opens the connection between this Python code and teh MySQL database"""
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
    """Displays all the of the necessary add ins to add a plant into the database (name, age, sunlight intake, etc.)"""
    try:
        cursor = connection.cursor()

        print("\n ADD NEW PLANT")
        print("=" * 30)

        name = input("Plant name: ").strip()
        age = input("Age (ex. 6 months, 2 years, 5 years): ").strip()

        print("\nSelect Plant Type:")
        cursor.execute("""
            SELECT type_id, type_name
            FROM plant_types
            ORDER BY type_id
        """)
        types = cursor.fetchall()

        for t in types:
            print(f"{t[0]}. {t[1]}")

        print("0. Add New Type")
        type_id = int(input("Type ID: "))

        if type_id == 0:
            new_type = input("Enter new plant type: ").strip()
            cursor.execute("INSERT INTO plant_types (type_name) VALUES (%s)", (new_type,))
            connection.commit()
            type_id = cursor.lastrowid
        

        print("\nSelect Size:")
        cursor.execute("""
            SELECT size_id, size_name
            FROM sizes
            ORDER BY size_id
        """)
        sizes = cursor.fetchall()

        for s in sizes:
            print(f"{s[0]}. {s[1]}")

        size_id = int(input("Size ID: "))

        print("\nSelect Location:")
        cursor.execute("""
            SELECT location_id, location_name
            FROM locations
            ORDER BY location_id
        """)
        locations = cursor.fetchall()

        for l in locations:
            print(f"{l[0]}. {l[1]}")

        print("0. Add New Location")
        location_id = int(input("Location ID: "))

        if location_id == 0:
            new_location = input("Enter new location: ").strip()
            cursor.execute("INSERT INTO locations (location_name) VALUES (%s)", (new_location,))
            connection.commit()
            location_id = cursor.lastrowid

        print("\nSelect Sunlight Level:")
        cursor.execute("""
            SELECT sunlight_id, level
            FROM sunlight_levels
            ORDER BY sunlight_id
        """)
        sunlight = cursor.fetchall()

        for s in sunlight:
            print(f"{s[0]}. {s[1]}")

        sunlight_id = int(input("Sunlight ID: "))
        

        cursor.execute("""
            INSERT INTO plants (name, age, type_id, size_id, location_id, sunlight_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (name, age, type_id, size_id, location_id, sunlight_id))

        connection.commit()

        print("Plant added successfully!")

    except Exception as e:
        print("Error:", e)

def view_plants(connection):
    """Option to view all of the plants that have been added into the database"""
    try:
        cursor = connection.cursor()

        query = """
        SELECT 
            p.name,
            p.age,
            t.type_name,
            s.size_name,
            l.location_name,
            sl.level
        FROM plants p
        JOIN plant_types t ON p.type_id = t.type_id
        JOIN sizes s ON p.size_id = s.size_id
        JOIN locations l ON p.location_id = l.location_id
        JOIN sunlight_levels sl ON p.sunlight_id = sl.sunlight_id
        ORDER BY p.plant_id
        """

        cursor.execute(query)
        plants = cursor.fetchall()

        print("\nALL PLANTS")
        print("=" * 80)

        print("-" * 80)

        for p in plants:
            print(f"{p[0]} | {p[1]} | {p[2]} | {p[3]} | {p[4]} | {p[5]}")
    except Exception as e:
        print("Error viewing plants:", e)

def update_plant(connection):
    """Option to update an added plant from the database"""
    try:
        cursor = connection.cursor()

        print("\nUPDATE PLANT")
        print("=" * 30)

        # Show plants
        cursor.execute("SELECT plant_id, name FROM plants ORDER BY plant_id")
        plants = cursor.fetchall()

        for p in plants:
            print(f"{p[0]}. {p[1]}")

        plant_id = input("\nEnter Plant ID to update: ")

        print("\nWhat do you want to update?")
        print("1. Name")
        print("2. Age")

        choice = input("Choice: ")

        if choice == "1":
            new_name = input("New name: ")

            cursor.execute("""
                UPDATE plants
                SET name = %s
                WHERE plant_id = %s
            """, (new_name, plant_id))

        elif choice == "2":
            new_age = input("New age: ")

            cursor.execute("""
                UPDATE plants
                SET age = %s
                WHERE plant_id = %s
            """, (new_age, plant_id))

        else:
            print("Invalid choice")
            return

        connection.commit()
        print("Plant updated successfully!")

    except Exception as e:
        print("Error updating plant:", e)

def delete_plant(connection):
    """Option to delete an added plant from the databade"""
    try:
        cursor = connection.cursor()

        print("\nDELETE PLANT")
        print("=" * 30)

        cursor.execute("SELECT plant_id, name FROM plants ORDER BY plant_id")
        plants = cursor.fetchall()

        for p in plants:
            print(f"{p[0]}. {p[1]}")

        plant_id = input("\nEnter Plant ID to delete: ")

        confirm = input("Are you sure? (yes/no): ").lower()

        if confirm != "yes":
            print("Cancelled")
            return

        cursor.execute("""
            DELETE FROM plants
            WHERE plant_id = %s
        """, (plant_id,))

        connection.commit()

        print("Plant deleted successfully!")

    except Exception as e:
        print("Error deleting plant:", e)
