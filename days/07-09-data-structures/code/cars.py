import re

cars = {
    "Ford": ["Falcon", "Focus", "Festiva", "Fairlane"],
    "Holden": ["Commodore", "Captiva", "Barina", "Trailblazer"],
    "Nissan": ["Maxima", "Pulsar", "350Z", "Navara"],
    "Honda": ["Civic", "Accord", "Odyssey", "Jazz"],
    "Jeep": ["Grand Cherokee", "Cherokee", "Trailhawk", "Trackhawk"],
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""

    all_jeeps = ", ".join(cars["Jeep"])
    return all_jeeps


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""

    first_models = [v[0] for k, v in cars.items()]
    return first_models


def get_all_matching_models(cars=cars, grep="trail"):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""

    # for models in cars.values():
    #     for model in models:
    #         m = model

    matching_models = [
        model
        for models in cars.values()
        for model in models
        if re.search(grep, model, re.IGNORECASE) is not None
    ]
    matching_models.sort()
    return matching_models


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""

    sorted_models = {}
    for k, v in cars.items():
        sorted_models[k] = v
        sorted_models[k].sort()
    return sorted_models


def main():
    all_jeeps = get_all_jeeps()
    first_models = get_first_model_each_manufacturer()
    matching_models = get_all_matching_models()
    sorted_models = sort_car_models()


if __name__ == "__main__":
    main()
