from random import randint, choice


GAME_RULE = 'What is the result of the expression?'


def get_question_and_right_answer():
    numb = randint(1, 21)
    numb_2 = randint(1, 21)
    operator = choice("+-*")
    question, answer = calculations(numb, numb_2, operator)

    return question, answer


def calculations(numb, numb_2, operator):
    if operator == "+":
        question = f'{numb} + {numb_2}'
        answer = numb + numb_2
    elif operator == "-":
        question = f'{numb} - {numb_2}'
        answer = numb - numb_2
    elif operator == "*":
        question = f'{numb} * {numb_2}'
        answer = numb * numb_2

    return question, answer
