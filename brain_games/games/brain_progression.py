from random import randint


GAME_RULE = 'What number is missing in the progression?'


def main():
    numb = randint(1, 16)
    numb_2 = randint(1, 6)
    numb_3 = randint(1, 10)
    iteration = 1

    question = ''
    for i in range(1, 11):
        if iteration == numb_3:
            question += '..' + ' '
            answer = numb
        else:
            question += str(numb) + ' '
        numb += numb_2
        iteration += 1

    return question, answer
