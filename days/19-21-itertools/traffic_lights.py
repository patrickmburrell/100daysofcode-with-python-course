import random
import sys
import time
from itertools import cycle


def main():
    colors = cycle(["red", "green", "amber"])

    while True:
        sys.stdout.write("\rTraffic light: " + next(colors) + "  ")
        sys.stdout.flush()

        delay = 2 + random.randint(0,3)
        time.sleep(delay)


if __name__ == "__main__":
    main()
