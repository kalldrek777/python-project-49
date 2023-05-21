from random import randint
import prompt
from brain_games import cli


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    numb = randint(1, 21)

    if numb % 2 == 0:
        point = 'yes'
    else:
        point = 'no'

    print(f'Question: {numb}')
    g = prompt.string('Your answer: ')

    if g != point:
        print(f"{g} is wrong answer ;(."
              f" Correct answer was {point}. Let's try again, {cli.name}!")
        return False
    else:
        print('Correct!')


if __name__ == "__main__":
    main()
