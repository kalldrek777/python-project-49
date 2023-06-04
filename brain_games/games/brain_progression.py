from random import randint


GAME_RULE = 'What number is missing in the progression?'


def get_question_and_right_answer():
    numb = randint(1, 16)
    numb_diff = randint(1, 6)
    empty_iteration = randint(1, 10)
    iteration = 1

    question = ''
    for i in range(1, 11):
        if iteration == empty_iteration:
            question += '..' + ' '
            answer = numb
        else:
            question += str(numb) + ' '
        numb += numb_diff
        iteration += 1

    return question, answer
