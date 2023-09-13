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
    pass
    names =[]
    for food in spicy_foods:
        names.append(food["name"])
    return names
print(get_names(spicy_foods))


def get_spiciest_foods(spicy_foods):
    pass
    spiciest_foods = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_foods.append(food)
    return spiciest_foods
   

def print_spicy_foods(spicy_foods):
    pass
    for food in spicy_foods:
        print(f"{food['name']} {'🌶️' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass
    matching_foods = []
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            matching_foods.append(food)
    return matching_foods


def print_spiciest_foods(spicy_foods):
    pass
    spiciest_foods = get_spiciest_foods(spicy_foods)
    for food in spiciest_foods:
        print(f"{food['name']} {'🌶️' * food['heat_level']}")


def get_average_heat_level(spicy_foods):
    pass
    heat_levels = [food["heat_level"] for food in spicy_foods]
    return sum(heat_levels) / len(heat_levels)

def create_spicy_food(spicy_foods, spicy_food):
    pass
    spicy_foods.append(spicy_food)
    return spicy_foods
