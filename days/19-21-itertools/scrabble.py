import itertools
import more_itertools
import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = "dictionary.txt"
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(
    f"https://bites-data.s3.us-east-2.amazonaws.com/{DICT}", DICTIONARY
)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""

    draw = [letter.lower() for letter in draw]

    words_of_length_n = []
    for length in range(2, len(draw) + 1):
        possible_words = _get_permutations_draw(draw, length)
        words = [
            possible_word
            for possible_word in possible_words
            if possible_word in dictionary
        ]
        words_of_length_n.append(words)
    words = list(more_itertools.flatten(words_of_length_n))
    return words


def _get_permutations_draw(draw, length):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""

    return ["".join(p) for p in itertools.permutations(draw, length)]


def main():
    tiles = "T, I, I, G, T, T, L"
    # tiles = "O, N, V, R, A, Z, H"
    # tiles = "E, P, A, E, I, O, A"
    # tiles = "B, R, C, O, O, E, O"
    # tiles = "G, A, R, Y, T, E, V"

    draw = [letter.strip().lower() for letter in tiles.split(",")]
    words = get_possible_dict_words(draw)
    pass


if __name__ == "__main__":
    main()
