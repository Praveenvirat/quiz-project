class Question:

    def __init__(self, question, choice1, choice2, choice3, choice4, answer):
        self.question = question
        self.choice1 = choice1
        self.choice2 = choice2
        self.choice3 = choice3
        self.choice4 = choice4
        self.answer = answer

    def is_answer_correct(self, ans):
        if self.answer == ans:
            return True
        else:
            return False