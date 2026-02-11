import random


textfile = open("questions.txt", "r")
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

    def removequestion(self, question):
        self.questions.remove(question)
            
    def getrandomquestion(self):
        randomindex = random.randint(0, len(self.questions) - 1)
        removedquestion = self.questions[randomindex]
        self.removequestion(removedquestion)
        return removedquestion

def main():
    question1 = question(lines[0], [lines[1], lines[2], lines[3], lines[4]], 0)
    question2 = question(lines[5], [lines[6], lines[7], lines[8], lines[9]], 1)
    question3 = question(lines[10], [lines[11], lines[12], lines[13], lines[14]], 2)
    question4 = question(lines[15], [lines[16], lines[17], lines[18], lines[19]], 3)
    question5 = question(lines[20], [lines[21], lines[22], lines[23], lines[24]], 0)

    bank = questionbank()
    bank.addquestion(question1)
    bank.addquestion(question2)
    bank.addquestion(question3)
    bank.addquestion(question4)
    bank.addquestion(question5)

    print(bank.getrandomquestion)