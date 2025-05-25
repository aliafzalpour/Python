import string
from tkinter import *
from random import choice
from tkinter import messagebox
import pyperclip
import json


#-------------------PASSWORD GENERATOR-------------------#
def password_generator():
    password_char = []
    generated_password = ""
    for _ in range(0,12):
        password_char += choice(string.ascii_uppercase)
        password_char += choice(string.ascii_lowercase)
        password_char += choice(string.digits)
        password_char += choice(string.punctuation)
    for _ in range(0,12):
        generated_password += password_char[choice(range(len(password_char)))]
    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)
#-------------------SAVE PASSWORD-------------------#
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if len(website) < 8:
        messagebox.showerror("Error", "Please enter your website")
    if len(username) < 3:
        messagebox.showerror("Error", "Please enter your username")
    if len(password) < 8:
        messagebox.showerror("Error", "Please enter your password")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {website}\nUsername: {username}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            new_data ={
                website : {
                    "username" : username,
                    "password" : password,
                }
            }
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)
#-------------------FIND PASSWORD-------------------#
def find_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo("Error", "No Data File Found")
    else:
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo("website", f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showerror("Error", f"No details for {website} found")

#-------------------UI SETUP-------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

password_logo = PhotoImage(file='password.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(120, 100, image=password_logo)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(window, text="Website")
website_label.grid(row=1, column=0)
email_label = Label(window, text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(window, text="Password")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(window, width=27)
website_entry.grid(row=1, column=1)
website_entry.insert(0, "<WEBSITE>")
website_entry.focus()
username_entry = Entry(window, width=27)
username_entry.grid(row=2, column=1)
username_entry.insert(0, "<EMAIL>")
password_entry = Entry(window, width=27)
password_entry.grid(row=3, column=1)
password_entry.insert(0, "<PASSWORD>")

#Buttons
password_generator_button = Button(text="Generate Password", width=14, command=password_generator)
password_generator_button.grid(row=3, column=2)
add_button = Button(window, text="Add Password", width=43, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(window, text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()