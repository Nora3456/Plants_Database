from database import *

def main():
    conn = create_connection()
    if not conn:
        return

    while True:
        print("\nPlant Manager")
        print("1. Add Plant")
        print("2. View Plants")
        print("3. Exit")

        choice = input("Choice: ")

        if choice == "1":
            name = input("Enter plant name: ")
            add_plant(conn, name)

        elif choice == "2":
            view_plants(conn)

        elif choice == "3":
            break

    conn.close()

if __name__ == "__main__":
    main()