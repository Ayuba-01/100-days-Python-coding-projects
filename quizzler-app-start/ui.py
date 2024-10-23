from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {0}", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas_background = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas_background.grid(column=0, row=1, columnspan=2, pady=50)

        self.question_text = self.canvas_background.create_text(150, 125, text=f"Question Text", fill=THEME_COLOR,
                                                                font=("Arial", 20, "italic"), width=280)

        correct_button_image = PhotoImage(file="./images/true.png")
        self.correct_button = Button(image=correct_button_image, highlightthickness=0, borderwidth=0,
                                     relief="raised", command=self.correct_button_func)
        self.correct_button.grid(column=0, row=2)

        wrong_button_image = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=wrong_button_image, highlightthickness=0, borderwidth=0,
                                   relief="raised", command=self.wrong_button_func)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        question_text = self.quiz.next_question()
        self.canvas_background.itemconfigure(self.question_text, text=question_text)

    def correct_button_func(self):
        response = self.quiz.check_answer("True")
        if response is True:
            self.canvas_background.config(bg="green")
        else:
            self.canvas_background.config(bg="red")

    def wrong_button_func(self):
        response = self.quiz.check_answer("False")
        if response is False:
            self.canvas_background.config(bg="green")
        else:
            self.canvas_background.config(bg="red")