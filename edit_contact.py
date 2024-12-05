def edit_contact(contact):
    name = input("Enter name of contact which want to edit: ")
    name.lower()
    if name in contact:
        print("Enter new contact details:")
        new_email = input("New email address: ")
        new_phone = input("New phone number: ")
        new_address = input("New address : ")

        contact[name]['email'] = new_email
        contact[name]['phone'] = new_phone
        contact[name]['address'] = new_address
        print("Contact has been updated. ")
    else:
        print("Entered contact not found. ")
