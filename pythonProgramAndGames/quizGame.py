'''
Caitlin Sheeran
01/06/2025
Python Quiz Game
https://www.youtube.com/watch?v=ix9cRaBkVe0&ab_channel=BroCode

'''

questions = ("How many elements are in the periodic table?: ",
            "Which animal lays the largest eggs?: ",
            "What is the most abundant gas in Earth's atmosphere?: ",
            "How many bones are in the human body?: ",
            "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")

guesses = []
score = 0
question_num = 0

for question in questions:
    print(f"------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()

    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print(f"Correct!")
    else:
        print(f"Incorrect")
        print(f"{answers[question_num]} is the correct answer")

    question_num +=1


print(f"------------------")
print(f"     RESULTS      ")
print(f"------------------")

print(f"Answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print(f"Guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")