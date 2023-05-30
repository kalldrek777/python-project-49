from random import randint


GAME_RULE = 'What is the result of the expression?'


def main():
    numb = randint(1, 21)
    numb_2 = randint(1, 21)
    a = randint(1, 3)

    if a == 1:
        question = f'{numb} + {numb_2}'
        answer = numb + numb_2
    elif a == 2:
        question = f'{numb} - {numb_2}'
        answer = numb - numb_2
    elif a == 3:
        question = f'{numb} * {numb_2}'
        answer = numb * numb_2

    return question, answer
