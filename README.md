Contact Management System

This Contact Management System is a Python-based application that allows users to add, edit, delete, and search for contacts. It also includes a feature to send email notifications when contacts are added, edited, or deleted, ensuring that users stay informed about changes to their contact list.

Features:
Add Contacts: Allows users to add new contacts with unique IDs.
Edit Contacts: Update the phone number of existing contacts.
Delete Contacts: Remove unwanted contacts from the system.
Search Contacts: Search for contacts by their unique ID.
List All Contacts: View all stored contacts in a list format.
Email Notifications: Automatically send email notifications when a contact is added, updated, or deleted.
Input Validation: Validates phone numbers and email addresses to ensure correctness.
Technologies Used
Python: Main programming language for the system.
CSV: Used for storing and managing contact data.
SMTP (Simple Mail Transfer Protocol): For sending email notifications.
Regular Expressions (Regex): Used for validating phone numbers and email addresses.
UUID: To generate unique contact IDs.

markdown
1. Add a new contact
2. List all contacts
3. Search for a contact
4. Edit a contact
5. Delete a contact
0. Exit
Adding a Contact:

You will be prompted to enter the name, phone number, email, and city.
The phone number must be 10 digits, and the email must follow a valid email format.
Editing a Contact:

Search for the contact using the unique ID, then enter a new phone number for the contact.
Deleting a Contact:

You can delete a contact by searching with the unique ID.
Email Setup
This project uses the Gmail SMTP server to send email notifications. To enable this feature, follow these steps:

Enable 2-Step Verification on your Gmail account.
Generate an App Password in your Google account security settings. Use this password in the code to log in via SMTP.
Update the following lines in the script with your email and the generated app password:
python
Copy code
from_email = "your-email@gmail.com"
password = "your-app-password"
Note: Storing email credentials directly in the code is not secure. For a production system, consider using environment variables or a more secure method of managing credentials.

Contact_ID, Name, Phone_Number, Email, City
Contact_ID: A unique identifier for each contact generated using UUID.
Name: The name of the contact.
Phone_Number: A 10-digit phone number.
Email: The email address of the contact.
City: The city where the contact resides.

License
This project is licensed under the MIT License. Feel free to use, modify, and distribute this project as you wish.
