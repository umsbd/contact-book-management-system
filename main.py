# This is a sample Python script.
from random import choice

from load_contact import load_contact

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
  #  print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
 #   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import addContact,delete_contact,edit_contact,loadContact,save_contact,view_contacts

contact = loadContact.load_contact()
while True:
    print("\n Contact Book Management Menu")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Save Contact")
    print("0. Exit")

    choice = input("Enter your choice:")
    if choice == '1':
        addContact.add_contact(contact)
    elif choice == '2':
        view_contacts.view_contacts(contact)
    elif choice == '3':
        edit_contact.edit_contact(contact)
    elif choice == '4':
        delete_contact.delete_contact(contact)
    elif choice == '5':
        save_contact.save_contact(contact)
    elif choice == '0':
        break
    else:
        print("Invalid choice. Please try again and use predefine menu key")