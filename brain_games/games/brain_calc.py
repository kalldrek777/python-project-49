from random import randint
import prompt
from brain_games import cli


def main():
    print('What is the result of the expression?')
    numb = randint(1, 21)
    numb_2 = randint(1, 21)
    a = randint(1, 3)

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


if __name__ == "__main__":
    main()
