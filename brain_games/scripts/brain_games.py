#!/usr/bin/env/ python3
from brain_games import cli
#from brain_games.cli import main as first
import prompt


def main():
    print('Welcome to the Brain Games!')
    #a = first()
    cli.main()
   # print(cli.name)
    #a = prompt.string('May i have your name? ')
    #print(f'Hello, {a}')
   # return cli.name


if __name__ == '__main__':
    main()
