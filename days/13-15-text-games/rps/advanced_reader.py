import csv
from pathlib import Path

from roll import Roll

BATTLE_DATA = "battle-table.csv"


def read_rolls():
    rolls = []

    folder = Path(__file__).parent
    with open(folder / BATTLE_DATA) as fin:
        reader = csv.DictReader(fin)
        for roll in reader:
            rolls.append(read_roll(roll))

    return rolls


def read_roll(row: dict):
    name = row["Attacker"]
    del row["Attacker"]
    del row[name]
    name = name.lower()

    greater_than = []
    lesser_than = []

    # print("Roll: {}".format(name))
    for k in row.keys():
        can_defeat = row[k].strip().lower() == "win"
        if can_defeat:
            greater_than.append(k)
        else:
            lesser_than.append(k)
        # print(" * {} will defeat {}? {}".format(name, k, can_defeat))

    roll = Roll(name, greater_than, lesser_than)
    return roll
