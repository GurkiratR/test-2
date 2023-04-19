phoneDirectory = {}

print("WELCOME TO THE GRANN'S PHONE DIRECTORY MENU")

while True:
    print("\n1. Add a record\n2. Search a record\n3. Change a record\n4. Delete a record\n5. Quit")
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter your 10-digit phone number: ")
        phoneDirectory[name] = phone
        print("Record added")

    elif choice == 2:
        name = input("Enter name to search: ")
        if name in phoneDirectory:
            print(name + ": " + phoneDirectory[name])
        else:
            print("Record not found")

    elif choice == 3:
        name = input("Enter name: ")
        if name in phoneDirectory:
            phone = input("Enter new 10-digit phone number: ")
            phoneDirectory[name] = phone
            print("Record updated")
        else:
            print("Record not found")

    elif choice == 4:
        name = input("Enter name: ")
        if name in phoneDirectory:
            del phoneDirectory[name]
            print("Record deleted")
        else:
            print("Record not found")

    elif choice == 5:
        print("Exiting phone directory...")
        break

    else:
        print("Invalid input. Please enter a number between 1 and 5.")

