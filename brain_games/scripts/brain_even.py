#!/usr/bin/env/ python3
from random import randint
import prompt
from brain_games.scripts.brain_games import main as f_main
from brain_games import cli


def main():
    b = f_main()
    a = 0
    while a<3:
        a += 1
        print('Answer "yes" if the number is even, otherwise answer "no".')
        numb = randint(1,21)


        if numb%2 == 0:
            point = 'yes'
        else:
            point = 'no'

	
        print(f'Question: {numb}')
        g = prompt.string('Your answer: ')


        if g!=point:
            print(f"{g} is wrong answer ;(. Correct answer was {point}. Let's try again, {cli.name}!")
            return False
        else:
            print('Correct!')


    print(f'Congratulations, {cli.name}')


if __name__ == "main":
    main()
