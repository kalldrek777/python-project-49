from random import randint


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_right_answer():
    question = randint(1, 21)

    answer = 'yes' if question % 2 == 0 else 'no'

    return question, answer
