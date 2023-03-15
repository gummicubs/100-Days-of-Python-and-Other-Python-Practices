class QuizBrain:
    
    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_number = 0
        self.score = 0
        
    def next_question(self):
        question = input(f"Q{self.question_number+1}. {self.questions_list[self.question_number].text} (True/False)?:")
        if question.lower() not in ['true', 'false']:
            print('You did not answer with a true or false. Please use only true or false.')
        else:
            if question.lower() == self.questions_list[self.question_number].answer.lower():
                print('You got it right!')
                self.score+=1
            else:
                print('You got it wrong.')
            print(f"The correct answer was: {self.questions_list[self.question_number].answer}.")
            print(f"Your current scroe is {self.score}/{self.question_number+1}")
            self.question_number+=1
        
        
    def still_have_questions(self):
        if self.question_number < len(self.questions_list):
            return True
        else:
            return False