# Задание 4.
# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

def get_equipment():
    LOAD_CAPACITY = 10000
    dict_back_pack = {'headlamp': 330, 'knife': 120, 'pillow': 400, 'notebook': 90, 'rope': 300, 'soap': 50,
                      'boots': 1100, 'food': 4700, 'water': 4500, 'axe': 900, 'raincoat': 350, 'pot': 470,
                      'first_aid_kit': 400, 'camping_stove': 2300, 'battery': 3400, 'fishing_rod': 1450,
                      'trousers': 760, 'hair_comb': 120, 'sweater': 570, 'blanket': 870}

    equipment = []
    for item, weight in dict_back_pack.items():
        if weight <= LOAD_CAPACITY:
            equipment.append(item)
            LOAD_CAPACITY -= weight
    return equipment


print(get_equipment())
