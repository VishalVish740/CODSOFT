# Task -- Contact Book Using Python
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contact_list(self):
        if not self.contacts:
            print("\nNo contacts record found.")
        else:
            print("\n ***** Contact List ***** ")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact.name}: {contact.phone}")

    def search_contact(self, search_term):
        search_results = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                search_results.append(contact)
        if not search_results:
            print("No matching contacts found.")
        else:
            print("\n***** Search Results *****")
            for i, contact in enumerate(search_results, start=1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone}")

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("\nEnter new details for the contact:")
                contact.phone = input("Phone: ")
                contact.email = input("Email: ")
                contact.address = input("Address: ")
                print("Contact updated successfully.")
                return
        print("\n Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_manager = ContactManager()
    while True:
        print("\n ***** Contact Management System *****")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(Contact(name, phone, email, address))
        elif choice == '2':
            contact_manager.view_contact_list()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_manager.search_contact(search_term)
        elif choice == '4':
            name = input("Enter name of contact to update: ")
            contact_manager.update_contact(name)
        elif choice == '5':
            name = input("Enter name of contact to delete: ")
            contact_manager.delete_contact(name)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()