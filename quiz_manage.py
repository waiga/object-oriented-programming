class QuizManage:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1} : {current_question.text} (True press t / False press f) >>> ").upper()
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("got it right")
            return True
        else:
            print("That's wrong.")
            print(f'correct answer : {correct_answer.lower()}')
            print(f"current score: {self.score} / {self.question_number}")
            return False

