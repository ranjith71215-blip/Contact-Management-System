# contacts_manager.py
# Contact Management System - Week 3 Project

import json
import re
import csv
import os

DATA_FILE = "contacts_data.json"

# ---------------- Ensure JSON File Exists ---------------- #
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f, indent=4)   # start with empty contacts
    print(f"✅ Created new contacts file: {DATA_FILE}")

# ---------------- Validation Helpers ---------------- #

def validate_phone(phone):
    digits = re.sub(r'\D', '', phone)
    return (10 <= len(digits) <= 15, digits if 10 <= len(digits) <= 15 else None)

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# ---------------- File Operations ---------------- #

def save_to_file(contacts):
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=4)
    print("✅ Contacts saved to", DATA_FILE)

def load_from_file():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    print("✅ No existing contacts file found. Starting fresh.")
    return {}

# ---------------- CRUD Functions ---------------- #

def add_contact(contacts):
    print("\n--- ADD NEW CONTACT ---")
    while True:
        name = input("Enter contact name: ").strip()
        if not name:
            print("Name cannot be empty!")
            continue
        if name in contacts:
            print(f"Contact '{name}' already exists!")
            if input("Update instead? (y/n): ").lower() == 'y':
                update_contact(contacts, name)
            return
        break

    while True:
        phone = input("Enter phone number: ").strip()
        valid, cleaned = validate_phone(phone)
        if valid: break
        print("Invalid phone number! Please enter 10-15 digits.")

    email = input("Enter email (optional): ").strip()
    if email and not validate_email(email):
        print("Invalid email format! Skipping email.")
        email = None

    address = input("Enter address (optional): ").strip()
    group = input("Enter group (Friends/Work/Family/Other): ").strip() or "Other"

    contacts[name] = {
        "phone": cleaned,
        "email": email or None,
        "address": address or None,
        "group": group
    }
    print(f"✅ Contact '{name}' added successfully!")

def search_contacts(contacts, term):
    term = term.lower()
    return {n: i for n, i in contacts.items() if term in n.lower() or term in i['phone']}

def update_contact(contacts, name=None):
    if not name:
        name = input("Enter contact name to update: ").strip()
    if name not in contacts:
        print("Contact not found!")
        return

    print(f"\n--- UPDATE CONTACT: {name} ---")
    phone = input("New phone (Enter to skip): ").strip()
    if phone:
        valid, cleaned = validate_phone(phone)
        if valid: contacts[name]['phone'] = cleaned
        else: print("Invalid phone skipped.")

    email = input("New email (Enter to skip): ").strip()
    if email and validate_email(email): contacts[name]['email'] = email
    elif email: print("Invalid email skipped.")

    address = input("New address (Enter to skip): ").strip()
    if address: contacts[name]['address'] = address

    group = input("New group (Enter to skip): ").strip()
    if group: contacts[name]['group'] = group

    print(f"✅ Contact '{name}' updated successfully!")

def delete_contact(contacts):
    name = input("Enter contact name to delete: ").strip()
    if name in contacts:
        if input(f"Are you sure to delete '{name}'? (y/n): ").lower() == 'y':
            del contacts[name]
            print(f"✅ Contact '{name}' deleted.")
    else:
        print("Contact not found!")

def display_all(contacts):
    print(f"\n--- ALL CONTACTS ({len(contacts)} total) ---")
    for name, info in contacts.items():
        print("="*50)
        print(f"👤 {name}")
        print(f"📞 {info['phone']}")
        if info['email']: print(f"📧 {info['email']}")
        if info['address']: print(f"📍 {info['address']}")
        print(f"👥 {info['group']}")

# ---------------- Extra Features ---------------- #

def export_csv(contacts):
    with open("contacts_export.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email", "Address", "Group"])
        for n, i in contacts.items():
            writer.writerow([n, i['phone'], i['email'], i['address'], i['group']])
    print("✅ Contacts exported to contacts_export.csv")

def statistics(contacts):
    print("\n--- CONTACT STATISTICS ---")
    print("Total Contacts:", len(contacts))
    groups = {}
    for i in contacts.values():
        groups[i['group']] = groups.get(i['group'], 0) + 1
    for g, c in groups.items():
        print(f"  {g}: {c} contact(s)")

# ---------------- Menu System ---------------- #

def main():
    contacts = load_from_file()
    while True:
        print("\n==============================")
        print("          MAIN MENU")
        print("==============================")
        print("1. Add New Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Export to CSV")
        print("7. View Statistics")
        print("8. Exit")
        choice = input("Enter choice (1-8): ").strip()

        if choice == '1': add_contact(contacts)
        elif choice == '2':
            term = input("Enter name/phone to search: ")
            results = search_contacts(contacts, term)
            display_all(results)
        elif choice == '3': update_contact(contacts)
        elif choice == '4': delete_contact(contacts)
        elif choice == '5': display_all(contacts)
        elif choice == '6': export_csv(contacts)
        elif choice == '7': statistics(contacts)
        elif choice == '8':
            save_to_file(contacts)
            print("Thank you for using Contact Management System!")
            break
        else: print("Invalid choice!")

if __name__ == "__main__":
    main()
