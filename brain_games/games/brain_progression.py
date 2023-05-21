from random import randint
import prompt
from brain_games import cli


def main():
    print('What number is missing in the progression?')
    numb = randint(1, 16)
    numb_2 = randint(1, 6)
    numb_3 = randint(1, 10)
    iteration = 1


    string = 'Question: '
    for i in range(1, 11):
        if iteration == numb_3:
            string += '..' + ' '
            save = numb
        else:
            string += str(numb) + ' '
        numb += numb_2
        iteration += 1

    print(string)

    g = prompt.string('Your answer: ')

    if g != str(save):
        print(
            f"{g} is wrong answer ;(. Correct answer"
            f" was {save}.\nLet's try again, {cli.name}!"
        )
        return False
    else:
        print('Correct!')


if __name__ == "__main__":
    main()
