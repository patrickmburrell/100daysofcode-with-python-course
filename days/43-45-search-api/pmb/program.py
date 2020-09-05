import api
import webbrowser


def main():
    print()
    print("******* SEARCH TALK PYTHON *******")
    print()

    term = input("What keywords to search for? ")

    results = api.search(term)

    print()
    print(f"There are {len(results)} matching episodes:")

    for index, result in enumerate(results, 1):
        print(f"{index}. {result.title}")

    print()
    browse_choice = input("Input the result number you want to browse (0 for none): ")
    try:
        browse_index = int(browse_choice) - 1
        if browse_index != 0:
            result = results[browse_index]
            relative_url = result.url
            full_url = f"http://talkpython.fm{relative_url}"
            webbrowser.open(full_url, new=2)
    except ValueError:
        print("Oops! Enter a result number.")
    except IndexError:
        print("Oops! Choose a number from those listed.")


if __name__ == "__main__":
    main()
