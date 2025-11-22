import tkinter as tk
import mysql.connector
from tkinter import messagebox

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="302503",
    database="userpass_project",
    port=3306,
    autocommit=False
)

cursor = conn.cursor()

# Tkinter setup
root = tk.Tk()
root.title("Login")
root.geometry("500x500")

# Username
tk.Label(root, text="Username", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
username = tk.Entry(root, font=("Arial", 12))
username.grid(row=0, column=1, padx=10, pady=10)

# Password
tk.Label(root, text="Password", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
password = tk.Entry(root, show='*', font=("Arial", 12))
password.grid(row=1, column=1, padx=10, pady=10)

# Function to validate login
def login():
    user = username.get()
    pwd = password.get()

    if not user or not pwd:
        messagebox.showwarning("Input Error", "Please enter both username and password")
        return

    try:
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (user, pwd))
        result = cursor.fetchone()
        if result:
            messagebox.showinfo("Login Success", f"Welcome {user}!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    except Exception as e:
        messagebox.showerror("Error", f"Database error: {e}")

# Login button (use grid instead of pack)
tk.Button(root, text='Login', command=login).grid(row=2, column=1, pady=20)

root.mainloop()