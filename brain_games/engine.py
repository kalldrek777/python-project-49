import prompt


def main(module_game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(module_game.game_rool)
    a = 0
    while a < 3:
        a += 1
        if module_game.main(name) is False:
            return False
    print(f'Congratulations, {name}!')
