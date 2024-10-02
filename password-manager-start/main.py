from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2)

username_label = Label(text="Email/Username: ")
username_label.grid(column=0, row=2)
username_entry = Entry(width=35)
username_entry.insert(0, "yusufayuba.a11@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", width=10)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add Password", width=32)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()