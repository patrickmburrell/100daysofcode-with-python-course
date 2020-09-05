import csv
import os
from collections import defaultdict

data = []


def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, "data", "StarWars.csv")

    age_groups = defaultdict(int)

    with open(filename, "r", encoding="utf-8") as fin:
        reader = csv.DictReader(fin)

        for row in reader:
            age_group = row.get("Age")
            print(age_group)

            age_groups[age_group] += 1

    pass


def main():
    init()


if __name__ == "__main__":
    main()
