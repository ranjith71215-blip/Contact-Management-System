# test_contacts.py
# Unit tests for contacts_manager.py

import unittest
import os
import json
import contacts_manager as cm

class TestContactManager(unittest.TestCase):

    def setUp(self):
        # Start with a fresh contacts dictionary for each test
        self.contacts = {
            "Ranjith": {
                "phone": "9663229517",
                "email": "ranjith@example.com",
                "address": None,
                "group": "Friends"
            },
            "Rahul": {
                "phone": "98765432111",
                "email": "rahul@example.com",
                "address": None,
                "group": "Work"
            },
            "Harsha": {
                "phone": "9876543210",
                "email": "harsha@example.com",
                "address": None,
                "group": "Friends"
            },
            "Bhowmik": {
                "phone": "9786543210",
                "email": "bhowmik@gmail.com",
                "address": None,
                "group": "Friends"
            },
            "Radhika": {
                "phone": "9876054321",
                "email": "radhika@example.com",
                "address": None,
                "group": "Family"
            }
        }

    def test_validate_phone(self):
        valid, cleaned = cm.validate_phone("9876543210")
        self.assertTrue(valid)
        self.assertEqual(cleaned, "9876543210")

        valid, cleaned = cm.validate_phone("123")
        self.assertFalse(valid)
        self.assertIsNone(cleaned)

    def test_validate_email(self):
        self.assertTrue(cm.validate_email("test@example.com"))
        self.assertFalse(cm.validate_email("invalid-email"))

    def test_search_contacts(self):
        results = cm.search_contacts(self.contacts, "rad")
        self.assertIn("Radhika", results)
        self.assertEqual(results["Radhika"]["phone"], "9876054321")

    def test_update_contact(self):
        # Simulate update by directly modifying dictionary
        self.contacts["Rahul"]["phone"] = "9998887776"
        self.contacts["Rahul"]["email"] = "rahul.new@example.com"
        self.assertEqual(self.contacts["Rahul"]["phone"], "9998887776")
        self.assertEqual(self.contacts["Rahul"]["email"], "rahul.new@example.com")

    def test_delete_contact(self):
        del self.contacts["Harsha"]
        self.assertNotIn("Harsha", self.contacts)

    def test_save_and_load_file(self):
        # Save to file
        cm.save_to_file(self.contacts)
        self.assertTrue(os.path.exists(cm.DATA_FILE))

        # Load back
        loaded = cm.load_from_file()
        self.assertIn("Ranjith", loaded)
        self.assertEqual(loaded["Ranjith"]["phone"], "9663229517")

    def test_statistics(self):
        # Capture statistics output
        cm.statistics(self.contacts)
        # Just check counts
        self.assertEqual(len(self.contacts), 5)
        groups = [c["group"] for c in self.contacts.values()]
        self.assertIn("Friends", groups)
        self.assertIn("Work", groups)
        self.assertIn("Family", groups)

if __name__ == "__main__":
    unittest.main()
