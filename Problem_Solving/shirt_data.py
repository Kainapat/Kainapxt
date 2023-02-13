shirt_data = {}

def insert_data():
    name = input("Enter the name of the person: ")
    size = input("Enter the shirt size of the person: ")
    shirt_data[name] = size
    print("Data has been successfully inserted.")

def update_data():
    name = input("Enter the name of the person whose data you want to update: ")
    if name in shirt_data:
        size = input("Enter the updated shirt size of the person: ")
        shirt_data[name] = size
        print("Data has been successfully updated.")
    else:
        print("Person not found in the database.")

def search_data():
    name = input("Enter the name of the person you want to search for: ")
    if name in shirt_data:
        print("Shirt size:", shirt_data[name])
    else:
        print("Person not found in the database.")

def delete_data():
    name = input("Enter the name of the person you want to delete: ")
    if name in shirt_data:
        del shirt_data[name]
        print("Data has been successfully deleted.")
    else:
        print("Person not found in the database.")

def view_all_data():
    print("Name\tShirt Size")
    for name, size in shirt_data.items():
        print(name, "\t", size)

while True:
    print("Select an option:")
    print("1. Insert Data")
    print("2. Update/Modify Data")
    print("3. Search Data")
    print("4. Delete Data")
    print("5. View All Data")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        insert_data()
    elif choice == 2:
        update_data()
    elif choice == 3:
        search_data()
    elif choice == 4:
        delete_data()
    elif choice == 5:
        view_all_data()
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please try again.")