from random import randint
import math
import prompt


game_rool = 'Find the greatest common divisor of given numbers.'


def main(name):
    numb = randint(1, 51)
    numb_2 = randint(1, 51)

    print(f'Question: {numb} {numb_2}')
    point = math.gcd(numb, numb_2)

    g = prompt.string('Your answer: ')

    if g != str(point):
        print(f"{g} is wrong answer ;(. Correct answer was"
              f" {point}.\nLet's try again, {name}!")
        return False
    else:
        print('Correct!')
