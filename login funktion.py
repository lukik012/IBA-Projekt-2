from tkinter import *
import customtkinter as c
from tkinter import messagebox


master = c.CTk()
master.title("Login Form")
master.geometry('1083x693')
master.configure(fg_color='#757575')


def open_dashboard(role):
    dashboard_window = c.CTkToplevel(master)
    dashboard_window.title("Dashboard")

    if role == "admin":
        label = c.CTkLabel(dashboard_window, text="Admin Dashboard", font=("Tuffy", 24))
        label.pack(pady=20)
        admin_button = c.CTkButton(dashboard_window, text="Admin Actions", command=admin_actions)
        admin_button.pack(pady=10)
    else:
        label = c.CTkLabel(dashboard_window, text="User Dashboard", font=("Tuffy", 24))
        label.pack(pady=20)

def admin_actions():
    messagebox.showinfo(title="Admin", message="You have admin rights to modify the database.")


def login():
    username = username_entry.get()
    password = password_entry.get()

    users = {
        "Monique": {"password": "12345", "role": "admin"},
        "Lukas": {"password": "12345", "role": "admin"},
        "Marco": {"password": "12345", "role": "admin"},
        "Mick": {"password": "12345", "role": "admin"},
        "John": {"password": "12345", "role": "user"}
    }

    if username in users and users[username]["password"] == password:
        role = users[username]["role"]
        messagebox.showinfo(title="Login Success", message="You have successfully logged in.")
        open_dashboard(role)
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

frame = c.CTkFrame(master=master, fg_color='#757575')

login_label = c.CTkLabel(frame, text="NextPrint", fg_color='#757575', text_color="#FFFFFF", font=("Tuffy", 64))
login_label2 = c.CTkLabel(frame, text="Easy", fg_color='#757575', text_color="#228B22", font=("Tuffy", 64))
username_label = c.CTkLabel(frame, text="Username", fg_color='#757575', text_color="#FFFFFF", font=("Tuffy", 24))
username_entry = c.CTkEntry(frame)
password_entry = c.CTkEntry(frame, show="*")
password_label = c.CTkLabel(frame, text="Password", fg_color='#757575', text_color="#FFFFFF", font=("Tuffy", 24))
login_button = c.CTkButton(frame, text="Login", fg_color='#228B22', text_color="#FFFFFF", font=("Tuffy", 24), command=login)

login_label.grid(row=0, column=0, pady=40)
login_label2.grid(row=0, column=1, pady=40)
username_label.grid(row=1, column=0, columnspan=1, pady=5)
username_label.grid(row=1, column=0, columnspan=1)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()
master.mainloop()
