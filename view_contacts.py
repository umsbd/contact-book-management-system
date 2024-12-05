def view_contacts(contact):
    if not contact:
        print("No contact name found.")
    else:
        for name, details in contact.items():
            print(f"Name: {name}")
            print(f"Email: {details['email']}")
            print(f"Phone: {details['phone']}")
            print(f"Address: {details['address']}")
            print() # Print blank
            