import tkinter as tk
from tkinter import messagebox
import pymysql

# Connect to MySQL
mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="mydatabase"
)
mycursor = mydb.cursor()

# Tkinter GUI
root = tk.Tk()
root.title("CRUD Application")

# Function to insert data into the database
def insert_data():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    sql = "INSERT INTO users (name, age, email) VALUES (%s, %s, %s)"
    val = (name, age, email)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo("Success", "Data inserted successfully.")

# Function to fetch data from the database
def fetch_data():
    mycursor.execute("SELECT * FROM users")
    result = mycursor.fetchall()
    for row in result:
        print(row)

# Function to clear the entry fields
def clear_fields():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# Function to update data in the database
def update_data():
    id = id_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    sql = "UPDATE users SET name = %s, age = %s, email = %s WHERE id = %s"
    val = (name, age, email, id)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo("Success", "Data updated successfully.")

# Function to delete data from the database
def delete_data():
    id = id_entry.get()
    sql = "DELETE FROM users WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo("Success", "Data deleted successfully.")

# Entry fields
tk.Label(root, text="ID:").grid(row=0, column=0, padx=10, pady=5)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Name:").grid(row=1, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Age:").grid(row=2, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=3, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons
insert_button = tk.Button(root, text="Insert", command=insert_data)
insert_button.grid(row=5, column=0, padx=5, pady=5)

fetch_button = tk.Button(root, text="Fetch", command=fetch_data)
fetch_button.grid(row=5, column=1, padx=5, pady=5)

update_button = tk.Button(root, text="Update", command=update_data)
update_button.grid(row=5, column=2, padx=10, pady=5)

delete_button = tk.Button(root, text="Delete", command=delete_data)
delete_button.grid(row=5, column=3, padx=10, pady=5)

clear_button = tk.Button(root, text="Clear", command=clear_fields)
clear_button.grid(row=5, column=4, padx=10, pady=5)


root.mainloop()
#pip install pyinstaller
#pyinstaller --onefile app.py

