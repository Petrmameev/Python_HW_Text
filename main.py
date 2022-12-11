with open('recept.txt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        count_ingredients = int(f.readline())
        ingredients = []
        for i in range(count_ingredients):
            ingredient = f.readline().strip()
            ingredient_name, quantity, measure = ingredient.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        f.readline()
        cook_book[dish_name] = ingredients
    print(f'cook_book = {cook_book}')

