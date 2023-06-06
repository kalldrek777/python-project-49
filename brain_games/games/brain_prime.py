from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. ' \
            'Otherwise answer "no".'


def get_question_and_right_answer():
    question = randint(1, 51)
    operator = 0
    answer = if_prime(question, operator)

    return question, answer


def if_prime(question, operator):
    for i in range(2, question):
        if (question % i == 0):
            operator = operator + 1
    answer = 'yes' if operator <= 0 else 'no'
    return answer
