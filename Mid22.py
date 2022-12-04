#Emily Rusch

recipe_dict = {"milk":1, "flour":2.5, "oil":0.5, "eggs": 4, "vanilla extract": 0.125}
amount = recipe_dict.values()

for key in sorted(recipe_dict):
    print(key)


def histogram(word):
    index = 0
    ingredients = []
    for key in sorted(word):
        ingredients.append(key)
    ingredients.sort()
    return ingredients

print(histogram(recipe_dict))
print(amount)


