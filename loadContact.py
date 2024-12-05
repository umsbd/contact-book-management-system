def load_contact():
    contact = {}
    try:
        with open('contactbook.txt','r') as f:
            for line in f:
                name,email,phone,address = line.strip().split(',')
                contact[name] = {'email': email, 'phone':phone, 'address':address}
    except FileNotFoundError:
        pass
    return contact