from random import randint


GAME_RULE = 'What is the result of the expression?'


def get_question_and_right_answer():
    numb = randint(1, 21)
    numb_2 = randint(1, 21)
    operator = randint(1, 3)

    if operator == 1:
        question = f'{numb} + {numb_2}'
        answer = numb + numb_2
    elif operator == 2:
        question = f'{numb} - {numb_2}'
        answer = numb - numb_2
    elif operator == 3:
        question = f'{numb} * {numb_2}'
        answer = numb * numb_2

    return question, answer
