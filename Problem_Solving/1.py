# Initialize an empty dictionary to store key-value pairs
data = {}

while True:
    # Display menu options
    print("Select an operation:")
    print("1) Add")
    print("2) Edit")
    print("3) Delete")
    print("4) Exit")

    # Get user input
    choice = int(input("Enter your choice: "))

    # Add a key-value pair
    if choice == 1:
        key = input("Enter key: ")
        value = input("Enter value: ")
        data[key] = value
        print("Key-value pair added successfully")

    # Edit a key-value pair
    elif choice == 2:
        key = input("Enter key: ")
        if key in data:
            value = input("Enter new value: ")
            data[key] = value
            print("Value updated successfully")
        else:
            print("Key not found")

    # Delete a key-value pair
    elif choice == 3:
        key = input("Enter key: ")
        if key in data:
            del data[key]
            print("Key-value pair deleted successfully")
        else:
            print("Key not found")

    # Exit the program
    elif choice == 4:
        break

    # Invalid choice
    else:
        print("Invalid choice")