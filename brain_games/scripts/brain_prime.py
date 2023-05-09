#!/usr/bin/env/ python3
from random import randint
import prompt
from brain_games.scripts.brain_games import main as f_main
from brain_games import cli


def main():
    f_main()
    a = 0
    while a < 3:
        a += 1
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        numb = randint(1, 51)

        print(f'Question: {numb}')
        point = ''
        k = 0
        for i in range(2, numb // 2 + 1):
            if (numb % i == 0):
                k = k + 1
        if (k <= 0):
            point = 'yes'
        else:
            point = 'no'

        g = prompt.string('Your answer: ')

        if g != str(point):
            print(f"{g} is wrong answer ;(. Correct answer was" \
                  f" {point}.\nLet's try again, {cli.name}!")
            return False
        else:
            print('Correct!')

    print(f'Congratulations, {cli.name}!')


if __name__ == "main":
    main()
