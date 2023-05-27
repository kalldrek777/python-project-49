from random import randint
import prompt


game_rool = 'Answer "yes" if given number is prime. ' \
            'Otherwise answer "no".'


def main(name):
    numb = randint(1, 51)

    print(f'Question: {numb}')
    point = ''
    k = 0
    for i in range(2, numb):
        if (numb % i == 0):
            k = k + 1
    if (k <= 0):
        point = 'yes'
    else:
        point = 'no'

    g = prompt.string('Your answer: ')

    if g != str(point):
        print(f"{g} is wrong answer ;(. Correct answer was"
              f" {point}.\nLet's try again, {name}!")
        return False
    else:
        print('Correct!')
