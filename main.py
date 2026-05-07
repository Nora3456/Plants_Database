from database import *

def main():
    conn = create_connection()
    if not conn:
        return

    while True:
        print("\n1. Add Plant")
        print("2. View Plants")
        print("3. Update Plant")
        print("4. Delete Plant")
        print("5. Exit")

        choice = input("Choice: ")

        if choice == "1":
            name = input("Enter plant name: ")
            add_plant(conn)

        elif choice == "2":
            view_plants(conn)
        
        elif choice == "3":
            update_plant(conn)

        elif choice == "4":
            delete_plant(conn)

        elif choice == "5":
            break
        

    conn.close()

if __name__ == "__main__":
    main()