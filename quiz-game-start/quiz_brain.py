class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        question = self.question_list[self.question_number].text
        correct_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question} (True/False)?: ")
        self.check_answer(user_answer, correct_answer)
        print("\n")

    def still_has_questions(self):
        question_number = self.question_number
        question_list_length = len(self.question_list)
        return question_number < question_list_length

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            print(f"The correct answer was: {correct_answer}.")
            self.score += 1
            print(f"Your current score is: {self.score}/{self.question_number}")

        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}.")
            print(f"Your current score is: {self.score}/{self.question_number}")
