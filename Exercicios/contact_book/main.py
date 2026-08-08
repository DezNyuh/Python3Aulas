import json
import os

JSON_PATH = os.path.join(os.getcwd(), 'Exercicios', 'contact_book', 'contacts.json')

print('''==== CONTACT BOOK ====

1 - Add contact
2 - List contacts
3 - Search contact
4 - Delete contact
5 - Export to CSV
6 - Import from CSV
0 - Exit''')



class Contact():

    def __init__(self, name, phone, email) -> None:
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
        }

def contact_details():
    name = input('Name: ')
    phone = input('Phone: ')
    email = input('Email: ')
    return Contact(name, phone, email)

def write_json(contacts):
    list_contacts = []
    for contact in contacts:
        list_contacts.append(contact.to_dict())
    with open(JSON_PATH, 'w', encoding='utf8') as f:
        json.dump(list_contacts, f, indent=2)

def read_json():
    try:
        with open(JSON_PATH, 'r', encoding='utf8') as f:
            file_data = json.load(f)
        contacts = [
            Contact(**item)
            for item in file_data
        ]
    except (FileNotFoundError, json.JSONDecodeError):
        write_json([])
        return []
    
    return contacts

def add_contact():
    write_json(read_json() + [contact_details()])



    