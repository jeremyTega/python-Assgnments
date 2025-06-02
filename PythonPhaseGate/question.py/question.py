import random
def getRandom():
    return random.randint(1, 100)

num1 = 0;
num2 = 0;

#userLife = 2
numberOfQuestion = 0
AskQuestion = 1
finalScore = 0


while numberOfQuestion != 10:
        userLife = 2
        num1 = getRandom()
        num2 = getRandom()
        question = 0
        answer = num1 - num2

        while True:
                if userLife == 0:
                    break
                if num2 > num1:
                        question = int(input(f'Question {AskQuestion} what is the answer : {num2} - {num1}: '))
                        answer = num2 - num1

                else:
                    question = int(input(f'Question {AskQuestion} what is the answer : {num1} - {num2}: '))


                if question != answer:
                        userLife = userLife - 1
                elif question == answer:
                            finalScore = finalScore + 1
                            break

        AskQuestion = AskQuestion + 1
        numberOfQuestion = numberOfQuestion + 1





print(f'your final score is {finalScore}')





