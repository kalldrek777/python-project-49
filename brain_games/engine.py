from brain_games.scripts.brain_games import main as f_main
from brain_games import cli


def main(module_game):
    f_main()
    a = 0
    while a < 3:
        a += 1
        if module_game() == False:
            return False
    print(f'Congratulations, {cli.name}!')


if __name__ == '__main__':
    main()


