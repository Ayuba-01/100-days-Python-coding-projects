from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
random_card = {}
to_learn = {}

# ---------------------------- change word mechanism ------------------------------- #
try:
    new_file = pandas.read_csv("./data/new_list_to_learn.csv")
except FileNotFoundError:
    original_file = pandas.read_csv("./data/french_words.csv")
    df = pandas.DataFrame(original_file)
    to_learn = df.to_dict(orient="records")
else:
    df = pandas.DataFrame(new_file)
    to_learn = df.to_dict(orient="records")


def next_card():
    global random_card, flip_timer
    window.after_cancel(flip_timer)
    random_card = random.choice(to_learn)
    canvas.itemconfigure(word_label, text=f"{random_card['French']}", fill="black")
    canvas.itemconfigure(lang_label, text=f"French", fill="black")
    canvas.itemconfigure(canvas_image, image=front_card_image)
    flip_timer = window.after(3000, flip_card)


# ---------------------------- Flip card mechanism ------------------------------- #
def flip_card():
    canvas.itemconfigure(canvas_image, image=back_card_image)
    canvas.itemconfigure(lang_label, text="English", fill="white")
    canvas.itemconfigure(word_label, text=random_card["English"], fill="white")


# ---------------------------- Known and Unknown word mechanism ------------------------------- #
def known_word():
    global random_card
    to_learn.remove(random_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("./data/new_list_to_learn.csv", index=False)
    random_card = random.choice(to_learn)
    next_card()


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
                      command=known_word)
right_button.grid(column=1, row=1)

next_card()
window.mainloop()
