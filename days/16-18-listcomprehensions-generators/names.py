NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    new_names = [name.title() for name in names]
    return list(set(new_names))


def reverse_first_last_names(name):
    first, last = name.split()
    return f"{last} {first}"


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    rev_names = [reverse_first_last_names(name) for name in names]

    sorted_names = sorted(rev_names, reverse=True)

    surname_sorted_names = [reverse_first_last_names(name) for name in sorted_names]
    return surname_sorted_names


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    split_names = [name.split()[0] for name in names]
    sorted_names = sorted(split_names, key=len)
    return sorted_names[0]


def main():
    dedup_and_title_names = dedup_and_title_case_names(NAMES)
    surname_sorted_names = sort_by_surname_desc(NAMES)
    shortest_name = shortest_first_name(NAMES)


if __name__ == "__main__":
    main()
