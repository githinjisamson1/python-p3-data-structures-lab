spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    namesOfSpicyFoodsLc = [item.get("name", "Not found!")
                           for item in spicy_foods]

    return namesOfSpicyFoodsLc


def get_spiciest_foods(spicy_foods):
    heatLevelGreaterThan5 = [
        item for item in spicy_foods if item.get("heat_level") > 5]

    return heatLevelGreaterThan5


def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        print(
            f"{item.get('name')} ({item.get('cuisine')}) | Heat Level: {'🌶' * item.get('heat_level') }")


# print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):

    for item in spicy_foods:
        if item.get("cuisine") == cuisine:
            matchingCuisineDict = item

    return matchingCuisineDict


print(get_spicy_food_by_cuisine(spicy_foods, "American"))


def print_spiciest_foods(spicy_foods):
    for item in spicy_foods:
        if item.get("heat_level") > 5:
            print(
                f"{item.get('name')} ({item.get('cuisine')}) | Heat Level: {'🌶' * item.get('heat_level') }")


def get_average_heat_level(spicy_foods):
    sumOfAllHeatLevels = 0

    for item in spicy_foods:
        sumOfAllHeatLevels += item.get("heat_level")

    return int(sumOfAllHeatLevels/len(spicy_foods))


# print(get_average_heat_level(spicy_foods))


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
