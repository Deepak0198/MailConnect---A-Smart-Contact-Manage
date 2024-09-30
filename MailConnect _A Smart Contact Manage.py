import csv, re
import ssl
import smtplib
import re
import uuid

def send_Add_email(Name,Phone_number,Email,City,to):
    from_email = "golu09062005@gmail.com" #use your mail
    password ="Golu@123"  #should be 2 step verified and use app password here
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    subject = "Phone number sucessfully Added "
    context = ssl.create_default_context()

    # Binding Subject and body
    body=""
    body += "Name: {} days\n".format(Name)
    body += "Phone Number {}\n".format(Phone_number)
    body += "Email {}\n".format(Email)
    body += "City {}\n".format(City)

    message = "Subject: {}\n\n{}".format(subject, body)

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)
            server.login(from_email, password)
            server.sendmail(from_email, to, message)
    except Exception as e:
        print("Failed to send email:", e)

def send_Edit_email(Name,Phone_number,Email,City,to,edit):
    from_email = "golu09062005@gmail.com" #use your mail
    password ="Golu@123"  #should be 2 step verified and use app password here
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    
    context = ssl.create_default_context()
    # Binding Subject and body
    if(edit==True):
        subject = "CONTACT UPDATED SUCCESSFULLY"
        body=""
        body += "Name: {} \n".format(Name)
        body += "Phone Number {}\n".format(Phone_number)
        body += "Email {}\n".format(Email)
        body += "City {}\n".format(City)
    else:
        subject = "THIS CONTACT IS SUCCESSFULLY REMOVED"
        body=""
        body += "Name: {} \n".format(Name)
        body += "Phone Number {}\n".format(Phone_number)
        body += "Email {}\n".format(Email)
        body += "City {}\n".format(City)

    message = "Subject: {}\n\n{}".format(subject,body)

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)
            server.login(from_email, password)
            server.sendmail(from_email, to, message)
    except Exception as e:
        print("Failed to send email:", e)


#it define the function that allowws the user to add new number.
def add_contact():
# prompt the user for the contact's name, phone number, email, and cityS
    Contact_ID=str(uuid.uuid4().hex[:5])
    Name = input("Enter the Name for the contact: ")
    Phone_number = input("Enter the Phone number: ")
# it ensure that the phone number is valid (phone number check karta hai 10 se jada ya kaam na ho.)
    phone_regex = r"^\d{10}$"
    while not re.search(phone_regex, Phone_number):
        print("Invalid phone number. Please enter a 10-digit phone number.")
        Phone_number = input("Enter the Phone number: ")
    Email = input("Enter the Email: ")
    if (Email.endswith("@cgu-odisha.ac.in")):
        pass
    else:
         email_regex = r"^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,4}$"
         while not re.search(email_regex, Email):
             if (Email.endswith("@cgu-odisha.ac.in")):
                break
             print("Invalid email address. Please enter a valid email address.")
             Email = input("Enter the Email: ") 
                
    
    City = input("Enter the City: ")
    with open("contact.csv","a",newline='') as csv_file:
        writer=csv.writer(csv_file)
        writer.writerow([Contact_ID,Name,Phone_number,Email,City]) 
    print("Your Contact unique id is :  ",Contact_ID)
    send_Add_email(Name,Phone_number,Email,City,Email)
def list_all_contact():
     with open("contact.csv","r") as csv_file:
        reader=csv.reader(csv_file)
        a=1
        for row in reader:
            print("===================")
            print("User:- ",a)
            print("Contact Id:-",row[0])
            print("Name:- ",row[1])
            print("Phone Number:- ",row[2])
            print("Email:- ",row[3])
            print("City:- ",row[4],)
            print("===================\n")
            a+=1


def search_contact():
    unique=input("Enter the unique id: ")

    with open("contact.csv", "r") as csv_file:
        reader= csv.reader(csv_file)
        a=0
        b=0
        for row in reader:
            a=a+1
            if  row[0]==unique:
                print("===================")
                print("THIS IS YOUR SEARCHED CONTACT")
                print("Contact Id:-",row[0])
                print("Name:- ",row[1])
                print("Phone Number:- ",row[2])
                print("Email:- ",row[3])
                print("City:- ",row[4],)
                print("===================\n")
            else:
                b=b+1
        if(a==b):
          print("enter the correct CONTACT ID")

def edit_contact():
    with open('contact.csv', 'r') as file:
        contacts = list(csv.reader(file))
    unique=input("Enter the unique id: ")
    a=0
    b=0

    for i, contact in enumerate(contacts):
        b+=1
        if contact[0]==unique:
            contacts[i][2] = input("Enter a new number: ")
            Name=contacts[i][1]
            Phone_number=contacts[i][2]
            Email=contacts[i][3]
            City=contacts[i][4]
            send_Edit_email(Name,Phone_number,Email,City,Email,True)
        else :
            a=a+1
    if(a==b):
     print("enter the correct CONTACT ID")
    with open('contact.csv', 'w',newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

    
    
def delete():
    a=0
    b=0
    with open('contact.csv', 'r') as file:
        contacts = list(csv.reader(file))

    unique=input("Enter the unique id: ")

    with open('contact.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i, contact in enumerate(contacts):
           a=a+1
           if contact[0]==unique:
                Name=contacts[i][1]
                Phone_number=contacts[i][2]
                Email=contacts[i][3]
                City=contacts[i][4]
                send_Edit_email(Name,Phone_number,Email,City,Email,False)

                continue
           else:
            b=b+1
        if(a==b):
            print("Enter the correct CONTACT ID")

        writer.writerow(contact)
           

    send_Edit_email(Name,Phone_number,Email,City,Email,False)

    
while True:
    print("Welcome to contact Management System\n")
    print("                MAIN MENU")
    print("          =======================")
    print("          [1] Add a new contact \n          [2] List all contact \n          [3] Search for contact \n          [4] Edit a contact \n          [5] Delete a contact \n          [0] Exit \n          =======================")
    choice=int(input("Enter the choice: "))
    if choice==1:
        add_contact()
        print("CONTACT SUCCESSFULLY ADDED")
    elif choice==2:
        list_all_contact()
    elif choice==3:
        search_contact()
    elif choice==4:
        edit_contact()
        print("UPDATED SUCCESSFULLY")
    elif choice==5:
        delete()
        print("CONTACT  SUCCESSFULLY REMOVED")
    elif choice==0:
        break
    else:
        print("invalid choice")
