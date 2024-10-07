from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    username = username_entry.get().title()
    website = web_entry.get()
    password = password_entry.get()
    new_dict = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showwarning(title=website, message=f"You cannot leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Do you want to save this details for {website}?\n "
                                                              f"Email/Username: {username}\n Password: {password}")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    # Read
                    data_file = json.load(file)
                    # Update
                    data_file.update(new_dict)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    # Write
                    json.dump(new_dict, file, indent=4)
            else:
                with open("data.json", "w") as file:
                    # Write
                    json.dump(data_file, file, indent=4)
            finally:
                web_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- Search Functionality ------------------------------- #
def find_password():
    user_website = web_entry.get().title()
    try:
        with open("data.json", "r") as file:
            data_file = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message=f"Data not found")
    else:
        if user_website in data_file:
            username = data_file[user_website]["username"]
            password = data_file[user_website]["password"]
            messagebox.showinfo(f"{user_website} details",
                                message=f'Your details for {user_website} is '
                                        f'\nEmail/Username: {username}\nPassword: {password}')
            pyperclip.copy(password)
        else:
            messagebox.showwarning(title="Error", message=f"{user_website} details not found")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=logo_image)
canvas.grid(column=1, row=0)

web_label = Label(text="Website: ")
web_label.grid(column=0, row=1)
web_entry = Entry(width=21)
web_entry.focus()
web_entry.grid(column=1, row=1)

username_label = Label(text="Email/Username: ")
username_label.grid(column=0, row=2)
username_entry = Entry(width=35)
username_entry.insert(0, "yusufayuba.a11@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", width=10, command=generate_password)
generate_button.grid(column=2, row=3)

search_button = Button(text="Search", width=10, command=find_password)
search_button.grid(column=2, row=1)

add_button = Button(text="Add Password", width=32, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
