from random import randint
import prompt


game_rool = 'Answer "yes" if the number is even, otherwise answer "no".'


def main(name):
    numb = randint(1, 21)

    if numb % 2 == 0:
        point = 'yes'
    else:
        point = 'no'

    print(f'Question: {numb}')
    g = prompt.string('Your answer: ')

    if g != point:
        print(f"{g} is wrong answer ;(."
              f" Correct answer was {point}. Let's try again, {name}!")
        return False
    else:
        print('Correct!')
