from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question_bank.append(Question(i['text'], i['answer']))

new_quiz = QuizBrain(question_bank)


while new_quiz.still_have_questions():
    new_quiz.next_question()
    
print(f'Your final score was: {new_quiz.score}/{len(new_quiz.questions_list)}.')