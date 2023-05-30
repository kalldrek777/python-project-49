from random import randint


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    question = randint(1, 21)

    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'

    return question, answer
