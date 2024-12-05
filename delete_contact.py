def delete_contact(contact):
    name = input("Enter name of contact to delete: ")
    if name in contact:
        del contact[name]
        print("Contact has been deleted.")
    else:
        print("Contact name not found. ")