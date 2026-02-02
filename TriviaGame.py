import random

class question:
    question = str()
    answers = []
    solution = int()

    def __init__ (self, ask, responses, correct):
        self.question = ask
        self.answers = responses
        self.solution = correct

    def askquestion(self):
        print(question)
        for i in range(len(self.answers)):
            print(self.answers[i])

    def checkifcorrect(self):
        player_input = input("What is your answer?")
        