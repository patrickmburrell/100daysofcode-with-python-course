us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

states = [
    "Oklahoma",  # 0
    "Kansas",
    "North Carolina",
    "Georgia",
    "Oregon",
    "Mississippi",
    "Minnesota",
    "Colorado",
    "Alabama",
    "Massachusetts",  # 9
    "Arizona",
    "Connecticut",
    "Montana",
    "West Virginia",
    "Nebraska",
    "New York",
    "Nevada",
    "Idaho",
    "New Jersey",
    "Missouri",  # 19
    "South Carolina",
    "Pennsylvania",
    "Rhode Island",
    "New Mexico",
    "Alaska",
    "New Hampshire",
    "Tennessee",
    "Washington",
    "Indiana",
    "Hawaii",  # 29
    "Kentucky",
    "Virginia",
    "Ohio",
    "Wisconsin",
    "Maryland",
    "Florida",
    "Utah",
    "Maine",
    "California",
    "Vermont",  # 39
    "Arkansas",
    "Wyoming",
    "Louisiana",
    "North Dakota",
    "South Dakota",
    "Texas",
    "Illinois",
    "Iowa",
    "Michigan",
    "Delaware",  # 49
]

NOT_FOUND = "N/A"


def get_every_nth_state(states=states, n=10):
    """Return a list with every nth item (default argument n=10, so every
       10th item) of the states list above (remember: lists keep order)"""

    nth_states = [
        state for index, state in enumerate(states) if not (index + 1) % n and index > 0
    ]
    return nth_states


def get_state_abbrev(state_name, us_state_abbrev=us_state_abbrev):
    """Look up a state abbreviation by querying the us_state_abbrev
       dict by full state name, for instance 'Alabama' returns 'AL',
       'Illinois' returns 'IL'.
       If the state is not in the dict, return 'N/A' which we stored
       in the NOT_FOUND constant (takeaway: dicts are great for lookups)"""

    if not state_name in us_state_abbrev:
        return NOT_FOUND

    return us_state_abbrev[state_name]


def get_longest_state(data):
    """Receives data, which can be the us_state_abbrev dict or the states
       list (see above). It returns the longest state measured by the length
       of the string"""
    longest_state = ""

    for state in data:
        if len(state) > len(longest_state):
            longest_state = state

    return longest_state


def combine_state_names_and_abbreviations(
    us_state_abbrev=us_state_abbrev, states=states
):
    """Get the first 10 state abbreviations ('AL', 'AK', 'AZ', ...) from
       the us_state_abbrev dict, and the last 10 states from the states
       list (see above) and combine them into a new list. The resulting list
       has both sorted, so:
       ['AK', 'AL', 'AZ', ..., 'South Dakota', 'Tennessee', 'Texas', ...]
       (see also test_combine_state_names_and_abbreviations)"""

    abbrevs = list(us_state_abbrev.values())
    abbrevs.sort()
    first_10_abbrev = abbrevs[:10]

    states.sort()
    last_10_states = states[-10:]

    return first_10_abbrev + last_10_states


def main():
    nth_states = get_every_nth_state()
    alabama_abbrev = get_state_abbrev("Alabama")
    illinois_abbrev = get_state_abbrev("Illinois")
    nf_avbrev = get_state_abbrev("Ada")
    state_1 = get_longest_state(us_state_abbrev)
    state_2 = get_longest_state(states)
    combination = combine_state_names_and_abbreviations()

if __name__ == "__main__":
    main()
