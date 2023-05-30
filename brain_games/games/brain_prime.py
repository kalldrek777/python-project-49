from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. ' \
            'Otherwise answer "no".'


def main():
    question = randint(1, 51)
    k = 0
    for i in range(2, question):
        if (question % i == 0):
            k = k + 1
    if (k <= 0):
        answer = 'yes'
    else:
        answer = 'no'

    return question, answer
