from random import randint
import math


GAME_RULE = 'Find the greatest common divisor of given numbers.'


def get_question_and_right_answer():
    numb = randint(1, 51)
    numb_2 = randint(1, 51)

    question = f'{numb} {numb_2}'
    answer = math.gcd(numb, numb_2)

    return question, answer
