from random import randint
import math
from brain_games import cli
import prompt


def main():
    print('Find the greatest common divisor of given numbers.')
    numb = randint(1, 51)
    numb_2 = randint(1, 51)

    print(f'Question: {numb} {numb_2}')
    point = math.gcd(numb, numb_2)

    g = prompt.string('Your answer: ')

    if g != str(point):
        print(f"{g} is wrong answer ;(. Correct answer was"
              f" {point}.\nLet's try again, {cli.name}!")
        return False
    else:
        print('Correct!')


if __name__ == "__main__":
    main()
