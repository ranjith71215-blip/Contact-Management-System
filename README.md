# Contact Management System

### Author

Ranjith Kumar G

---

## Project Description

The Contact Management System is a Python-based console application that allows users to manage personal and professional contacts efficiently. Users can add, search, update, delete, view, and export contact information while storing data permanently using a JSON file.

This project demonstrates the use of Python fundamentals such as:

* Variables and Data Types
* Functions
* Conditional Statements (`if`, `elif`, `else`)
* Loops (`while`, `for`)
* Dictionaries
* File Handling (`JSON` and `CSV`)
* Regular Expressions (`re`)
* Input Validation
* Data Persistence
* Modular Programming

---

## Features

### Contact Management

The system provides the following operations:

| Feature        | Description                                             |
| -------------- | ------------------------------------------------------- |
| Add Contact    | Add a new contact with phone, email, address, and group |
| Search Contact | Search contacts by name or phone number                 |
| Update Contact | Modify existing contact details                         |
| Delete Contact | Remove a contact from the system                        |
| View Contacts  | Display all saved contacts                              |
| Export CSV     | Export contacts to a CSV file                           |
| Statistics     | View contact count by groups                            |

### Input Validation

* Contact name cannot be empty.
* Duplicate contacts are detected automatically.
* Phone numbers must contain 10–15 digits.
* Email addresses are validated using regular expressions.
* Invalid inputs are handled gracefully.

### Data Persistence

* Contacts are stored in a JSON file (`contacts_data.json`).
* Data is automatically loaded when the program starts.
* Data is saved when the user exits the application.

---

## Project Structure

```text
week3-contact-manager/
│── contacts_manager.py
│── contacts_data.json
│── test_contacts.py
│── README.md
│── requirements.txt
└── .gitignore
```

---

## How to Run

### Method 1: Run Normally

Open the terminal in VS Code and run:

```bash
python contact_management.py
```

---

### Method 2: Run from Command Prompt

```bash
python contact_management.py
```

The application will display the main menu and allow you to manage contacts interactively.

---

## Sample Menu

```text
==============================
          MAIN MENU
==============================
1. Add New Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Export to CSV
7. View Statistics
8. Exit
```

---

## Sample Data (contacts_data.json)

```json
{
    "Ranjith": {
        "phone": "9663229517",
        "email": "ranjith@example.com",
        "address": "null",
        "group": "Friends"
    },
    "Rahul": {
        "phone": "98765432111",
        "email": "rahul@example.com",
        "address": "null",
        "group": "Work"
    },
    "Harsha": {
        "phone": "9876543210",
        "email": "harsha@example.com",
        "address": "null",
        "group": "Friends"
    },
    "Bhowmik": {
        "phone": "9786543210",
        "email": "bhowmik@gmail.com",
        "address": "null",
        "group": "Friends"
    },
    "Radhika": {
        "phone": "9876054321",
        "email": "radhika@example.com",
        "address": "null",
        "group": "Family"
    }
}
```

---

## Sample Statistics Output

```text
--- CONTACT STATISTICS ---
Total Contacts: 5

Friends: 3 contact(s)
Work: 1 contact(s)
Family: 1 contact(s)
```

---

## Learning Outcomes

By completing this project, you will learn how to:

* Create and organize functions
* Work with dictionaries for data storage
* Validate user inputs using regular expressions
* Read and write JSON files
* Export data to CSV format
* Implement CRUD (Create, Read, Update, Delete) operations
* Build menu-driven console applications
* Handle persistent data storage
* Design modular Python programs

---

## Optimization Techniques

* Modular function-based design
* Reusable validation functions
* Dictionary-based contact storage for fast lookups
* Automatic JSON file creation if missing
* Efficient search using dictionary comprehensions
* Reduced code duplication through function reuse

---

## Technologies Used

* Python 3
* JSON
* CSV
* Regular Expressions (re)
* Visual Studio Code (VS Code)

---

## Conclusion

This Contact Management System is a practical Python application that combines file handling, input validation, regular expressions, dictionaries, and CRUD operations into a single project. It provides a strong foundation for developing more advanced applications such as database-driven contact managers, web applications, and customer relationship management (CRM) systems.
