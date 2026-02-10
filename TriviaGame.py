import random

textfile = open("triviaquestions.txt", "r")
lines = textfile.readlines()

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
        if player_input == "A" or player_input == "a":
            if 0 == self.solution:
                return True
            else:
                return False
        elif player_input == "B" or player_input == "a":
            if 1 == self.solution:
                return True
            else:
                return False
        elif player_input == "C" or player_input == "c":
            if 2 == self.solution:
                return True
            else:
                return False
        elif player_input == "D" or player_input == "d":
            if 3 == self.solution:
                return True
            else:
                return False
class questionbank:
    questions = []

    def __init__ (self):
        self.questions = []

    def addquestion(self, newquestion):
        self.questions.append(newquestion)

    def getrandomquestion(self):
        return random.choice(self.questions)
            
        