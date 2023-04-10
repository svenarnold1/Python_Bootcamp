from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# create a list that includes all the question we stored in our question_data python file
for dicts in question_data:
    question_text = dicts['text']
    question_answer = dicts['answer']
    question_bank.append(Question(q_text=question_text, q_answer=question_answer))


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
