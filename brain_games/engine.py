import prompt


def engine(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_RULE)
    rounds = 3
    for _ in range(rounds):
        question, correct_answer = game.get_question_and_right_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == str(correct_answer):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
