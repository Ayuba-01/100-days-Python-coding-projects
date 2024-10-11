from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
random_dict = {}

# ---------------------------- change word mechanism ------------------------------- #
with open("./data/french_words.csv") as file:
    f = pandas.read_csv(file)
    df = pandas.DataFrame(f)
    data_dict_list = df.to_dict(orient="records")


def next_card():
    global random_dict, flip_timer
    window.after_cancel(flip_timer)
    random_dict = random.choice(data_dict_list)
    canvas.itemconfigure(word_label, text=f"{random_dict['French']}", fill="black")
    canvas.itemconfigure(lang_label, text=f"French", fill="black")
    canvas.itemconfigure(canvas_image, image=front_card_image)
    flip_timer = window.after(3000, flip_card)


# ---------------------------- Flip card mechanism ------------------------------- #
def flip_card():
    global random_dict
    canvas.itemconfigure(canvas_image, image=back_card_image)
    canvas.itemconfigure(lang_label, text="English", fill="white")
    canvas.itemconfigure(word_label, text=random_dict["English"], fill="white")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)
canvas = Canvas(width=800, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card_image = PhotoImage(file="./images/card_front.png")
back_card_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 275, image=front_card_image)
lang_label = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word_label = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0, relief="raised",
                      command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, borderwidth=0, relief="raised",
                      command=next_card)
right_button.grid(column=1, row=1)

next_card()
window.mainloop()
