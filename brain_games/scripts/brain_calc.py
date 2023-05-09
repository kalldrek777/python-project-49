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
        print('What is the result of the expression?')
        numb = randint(1, 21)
        numb_2 = randint(1, 21)

        if a == 1:
            print(f'Question: {numb} + {numb_2}')
            point = numb + numb_2
        elif a == 2:
            print(f'Question: {numb} - {numb_2}')
            point = numb - numb_2
        elif a == 3:
            print(f'Question: {numb} * {numb_2}')
            point = numb * numb_2

        g = prompt.string('Your answer: ')

        if g != str(point):
            print(f"{g} is wrong answer ;(. Correct answer"
                  f" was {point}.\nLet's try again, {cli.name}!")
            return False
        else:
            print('Correct!')

    print(f'Congratulations, {cli.name}!')


if __name__ == "main":
    main()
