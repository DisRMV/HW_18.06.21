
def cook_book(file):
    cook_book = {}
    for lane in file:
        cook_book[lane.strip()] = []
        iteration = int(file.readline().strip())
        counter = 0
        while counter != iteration:
            ingredients = file.readline().strip().split('|')
            ingredients_dict = {}
            ingredients_dict['ingredient_name'] = ingredients[0]
            ingredients_dict['quantity'] = int(ingredients[1])
            ingredients_dict['measure'] = ingredients[2]
            cook_book[lane.strip()].append(ingredients_dict)
            counter += 1
        file.readline()
    return cook_book


def get_shop_list_by_dishes(cook_book, dishes_list, persons):
    shop_list = {}
    for dish in dishes_list:
        if dish in cook_book:
            for ing in cook_book[dish]:
                if ing['ingredient_name'] in shop_list:
                    shop_list[ing['ingredient_name']]['quantity'] += ing['quantity']*persons
                else:
                    shop_list[ing['ingredient_name']] = {'measure': ing['measure'], 'quantity': ing['quantity']*persons}
        else:
            return 'Ошибка'
    return shop_list


with open('recipes.txt', encoding='utf-8') as recipes:
    cook_book_ = cook_book(recipes)
    print(cook_book_)
    print(get_shop_list_by_dishes(cook_book_, ['Омлет', 'Утка по-пекински', 'Фахитос'], 3))


