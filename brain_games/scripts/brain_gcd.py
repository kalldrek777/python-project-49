#!/usr/bin/env/ python3
from random import randint
import prompt
from brain_games.scripts.brain_games import main as f_main
import math


def main():
    b = f_main()
    a = 0
    while a<3:
        a += 1
        print('Find the greatest common divisor of given numbers.')
        numb = randint(1,51)
        numb_2 = randint(1,51)


        print(f'Question: {numb} {numb_2}')
        point = math.gcd(numb, numb_2)

	
        g = prompt.string('Your answer: ')


        if g!=str(point):
            print(f"{g} is wrong answer ;(. Correct answer was {point}.\nLet's try again, {b}!")
            return False
        else:
            print('Correct!')


    print(f'Congratulations, {b}')


if __name__ == "main":
    main()
