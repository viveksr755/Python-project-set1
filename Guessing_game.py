
# The way of thinking before coding

'''
# list of questions
# store the answers
# randomly pick questions
# ask the questions
# see if they are correct
# keep track of the score
# tell the user their score'''





import random

questions = {
    "What is the keyword to define a function in Python?": "def",
    "Which data type is used to store True or False values?": "boolean",
    "What is the correct file extension for Python files?": ".py",
    "Which symbol is used to comment in Python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in Python?": "for",
    "What is the output of 2 ** 3 in Python?": "8",
    "What keyword is used to import a module in Python?": "import",
    "What does the len() function return?": "length",
    "What is the result of 10 // 3 in Python?": "3"
}


def game():

    question_list=list(questions.keys())
    total_questions=5
    score=0

    selected_questions=random.sample(question_list,total_questions)

    for indx, q in enumerate(selected_questions):
        print(f'{indx+1}. {q}')
        user_answer=input("answer: ").lower().strip()
        correct_answer=questions[q]

        if user_answer==correct_answer.lower():
            print("correct!\n")
            score+=1

        else:
            print(f'wrong, the correct answer is {correct_answer} ')

    print(f"Game over!, your score is {score}")




game()

