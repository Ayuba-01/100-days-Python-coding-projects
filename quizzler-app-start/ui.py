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
        self.canvas_background.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas_background.itemconfigure(self.question_text, text=question_text)
        else:
            self.canvas_background.itemconfigure(self.question_text, text="You have reached the end of the quiz."
                                                                          f"\n You score "
                                                                          f"{self.quiz.score}/"
                                                                          f"{len(self.quiz.question_list)} ")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def correct_button_func(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def wrong_button_func(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canvas_background.config(bg="green")
        else:
            self.canvas_background.config(bg="red")
        self.window.after(1000, self.get_next_question)
