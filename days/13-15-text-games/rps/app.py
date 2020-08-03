import random
from player import Player
from roll import Roll
from advanced_reader import read_rolls

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
MAX_ROUNDS = 3


def display_header():
    print("------------------------------")
    print("    Rock, Paper, Scissors")
    print("------------------------------")
    print()


def get_name():
    name = input("What is your name? ")
    print()
    return name


def get_advanced():
    adv = input("Want the advanced version? ")
    print()
    return adv == "y" or adv == "Y"


def get_rounds():
    while True:
        try:
            rounds = input("How many rounds? ")
            rounds = int(rounds)
            print()
            return rounds
        except:
            print("Please enter an integer")


def display_welcome(name):
    print(f"Welcome to the game, {name}!")
    print()


def display_outcome(message1, message2, message3):
    print(message1)
    print(message2)
    print(message3)
    print()


def build_rolls(advanced):
    if advanced:
        rolls = read_rolls()
    else:
        rolls = [
            Roll(ROCK, [SCISSORS], [PAPER]),
            Roll(PAPER, [ROCK], [SCISSORS]),
            Roll(SCISSORS, [PAPER], [ROCK]),
        ]
    return rolls


def get_roll_names(rolls):
    return [roll.name for roll in rolls]


def get_roll(rolls):
    roll_name = ""
    roll_names = get_roll_names(rolls)
    while roll_name not in roll_names:
        print("Available rolls:")
        for roll in rolls:
            print(f" - {roll.name}")
        roll_name = input("Enter your roll: ")
    print()
    roll = [roll for roll in rolls if roll.name == roll_name]
    return roll[0]


def pick_random_roll(rolls):
    return random.choice(rolls)


def game_loop(player1, player2, rolls, max_rounds):
    p1_wins = 0
    p2_wins = 0

    count = 0
    while count < max_rounds:
        print(f"Round: {count+1}")

        p1_roll = get_roll(rolls)
        p2_roll = pick_random_roll(rolls)

        p1_win = p1_roll.can_defeat(p2_roll)
        p2_win = p2_roll.can_defeat(p1_roll)

        message1 = f"{player1.name}: {p1_roll.name}"
        message2 = f"{player2.name}: {p2_roll.name}"

        if p1_win:
            message3 = f"{player1.name} WINS!"
            p1_wins += 1
        elif p2_win:
            message3 = f"{player2.name} WINS!"
            p2_wins += 1
        else:
            message3 = "TIE!"
        display_outcome(message1, message2, message3)

        count += 1

    message1 = f"{player1.name}: {p1_wins} wins"
    message2 = f"{player2.name}: {p2_wins} wins"
    if p1_wins > p2_wins:
        message3 = f"After {max_rounds} rounds, {player1.name} is the champion!"
    elif p2_win:
        message3 = f"After {max_rounds} rounds, {player2.name} is the champion!"
    else:
        message3 = (
            f"After {max_rounds} rounds, {player1.name} and {player2.name} are TIED!"
        )
    display_outcome(message1, message2, message3)


def main():
    display_header()
    name = get_name()
    display_welcome(name)

    advanced = get_advanced()

    rolls = build_rolls(advanced)
    max_rounds = get_rounds()

    player1 = Player(name)
    player2 = Player("Computer")

    game_loop(player1, player2, rolls, max_rounds)


if __name__ == "__main__":
    main()
