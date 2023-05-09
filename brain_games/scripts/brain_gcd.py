#!/usr/bin/env/ python3
from random import randint
import prompt
from brain_games.scripts.brain_games import main as f_main
import math
from brain_games import cli


def main():
    f_main()
    a = 0
    while a < 3:
        a += 1
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

    print(f'Congratulations, {cli.name}!')


if __name__ == "main":
    main()
