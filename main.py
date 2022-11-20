from question_model import Question
from data import question_data
from quiz_manage import QuizManage

question_bank = [Question(data["text"], data["answer"]) for data in question_data]

quiz = QuizManage(question_bank)

# when forget () 🥲
# print("no () : ", quiz.still_has_questions) # <bound method QuizManage.still_has_questions of <quiz_manage.QuizManage object at 0x7f94201dae80>>
# print("with () :", quiz.still_has_questions()) # True

while quiz.still_has_questions():
    quiz.next_question()

print("=" * 40)
print(f"Final Score 😄 : {quiz.score} / {quiz.question_number}")
print("=" * 40)
