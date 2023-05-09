#!/usr/bin/env/ python3
from random import randint
import prompt
from brain_games.scripts.brain_games import main as f_main
import math
from brain_games import cli


def main():
    b = f_main()
    a = 0
    while a<3:
        a += 1
        print('Find the greatest common divisor of given numbers.')
        numb = randint(1,16)
        numb_2 = randint(1,6)
        numb_3 = randint(1,11)
        iteration = 1
    

        string = 'Question: '
        for i in range(1,11): 
            if iteration == numb_3:
                string += '..' + ' '
                save = numb
            else:
                string += str(numb) + ' '
            numb += numb_2
            iteration += 1


        print(string)
        

        g = prompt.string('Your answer: ')


        if g!=str(save):
            print(f"{g} is wrong answer ;(. Correct answer was {save}.\nLet's try again, {cli.name}!")
            return False
        else:
            print('Correct!')


    print(f'Congratulations, {cli.name}!')


if __name__ == "main":
    main()
