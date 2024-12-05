def save_contact(contact):
    with open('contactbook.txt','w') as f:
        for name, details in contact.items():
            f.write(f"{name},{details['email']},{details['phone']},{details['address']}\n")
    print("Contacts has been save in contactbook.txt successfully.")