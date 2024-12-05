def add_contact(contact):
    name = input("Enter contact name: ")
    name = name.lower()
    if name in contact:
        print("Contact name already exists !!!")
        return
    email = input("Enter email address: ")
    phone = input("Enter phone number: ")
    address = input("Enter address : ")

    contact[name] = {'email':email,'phone':phone,'address':address}
    print("Contact added successfully. ")