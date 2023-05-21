#!/usr/bin/env/ python3
from brain_games.games.brain_gcd import main as game_module
from brain_games.engine import main as engine


def main():
    engine(game_module)


if __name__ == "__main__":
    main()
