import json
import tkinter as tk

# function to save passwords to a JSON file
def save_passwords(username, password):
    try:
        with open('passwords.json', 'r') as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = {}
    passwords[username] = password
    with open('passwords.json', 'w') as file:
        json.dump(passwords, file)

# function to retrieve passwords from the JSON file
def get_password(username):
    with open('passwords.json', 'r') as file:
        passwords = json.load(file)
    return passwords.get(username)

# function to handle the "Save" button click event
def save_button_click():
    username = username_entry.get()
    password = password_entry.get()
    save_passwords(username, password)
    status_label.config(text=f"Saved password for {username}")

# function to handle the "Retrieve" button click event
def retrieve_button_click():
    username = username_entry.get()
    password = get_password(username)
    if password:
        status_label.config(text=f"The password for {username} is {password}")
    else:
        status_label.config(text="Password not found")

# create the main window and widgets
root = tk.Tk()
root.title("Password Manager")

username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

save_button = tk.Button(root, text="Save", command=save_button_click)
save_button.pack()

retrieve_button = tk.Button(root, text="Retrieve", command=retrieve_button_click)
retrieve_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

# start the main event loop
root.mainloop()


