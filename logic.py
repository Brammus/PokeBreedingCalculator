from random import randint
# used for calculating possible IV outcomes for Pokemon with 2 inputs, parent 1 and parent 2 (including items)


def get_random_iv_to_set(ivs):
    ivs_left = []
    for iv in ivs:
        if ivs[iv] is None:
            ivs_left.append(iv)
    random_stat_index = randint(0, (len(ivs_left)-1))
    random_stat = ivs_left[random_stat_index]
    return random_stat


power_items = {'Power Weight': 'HP', 'Power Bracer': 'Attack', 'Power Belt': 'Defence', 'Power Lens': 'Special Attack',
               'Power Band': 'Special Defence', 'Power Anklet': 'Speed'}

# initialize list if IV's to get for baby
baby_pokemon = {
    'individual_values': {
        'HP': None,
        'Attack': None,
        'Defence': None,
        'Special Attack': None,
        'Special Defence': None,
        'Speed': None
    }
}
parent_1 = {
    'individual_values': {
        'HP': 31,
        'Attack': 30,
        'Defence': 31,
        'Special Attack': 15,
        'Special Defence': 24,
        'Speed': 31
    },
    'held_item': 'Destiny Knot'
}
parent_2 = {
    'individual_values': {
        'HP': 16,
        'Attack': 18,
        'Defence': 10,
        'Special Attack': 15,
        'Special Defence': 31,
        'Speed': 15
    },
    'held_item': 'Power Band'
}

ivs_to_set = 3
if parent_1['held_item'] == 'Destiny Knot' or parent_2['held_item'] == 'Destiny Knot':
    ivs_to_set = 5

parent_power_items = 0
if parent_1['held_item'] in power_items:
    parent_power_items += 1
elif parent_2['held_item'] in power_items:
    parent_power_items += 1

parent_power_inherit = 0
if parent_power_items == 2:
    parent_power_inherit = randint(1, 2)
elif parent_power_items == 1:
    if parent_1['held_item'] in power_items:
        parent_power_inherit = 1
    elif parent_2['held_item'] in power_items:
        parent_power_inherit = 2

if parent_power_items > 0 and parent_power_inherit == 1:
    # inherit from parent_1
    parent_item = parent_1['held_item']
    item_stat = power_items[parent_item]
    parent_stat = parent_1['individual_values'][item_stat]
    baby_pokemon['individual_values'][item_stat] = parent_stat
    ivs_to_set = ivs_to_set - 1
elif parent_power_items > 0 and parent_power_inherit == 2:
    # inherit from parent_2
    parent_item = parent_2['held_item']
    item_stat = power_items[parent_item]
    parent_stat = parent_2['individual_values'][item_stat]
    baby_pokemon['individual_values'][item_stat] = parent_stat
    ivs_to_set = ivs_to_set - 1


# inheriting IVs
for iv in range(ivs_to_set):
    # pick random iv
    stat_to_set = get_random_iv_to_set(baby_pokemon['individual_values'])
    random_parent = randint(1, 2)

    if random_parent == 1:
        baby_pokemon['individual_values'][stat_to_set] = parent_1['individual_values'][stat_to_set]
    else:
        baby_pokemon['individual_values'][stat_to_set] = parent_2['individual_values'][stat_to_set]

# setting leftover IVs
for iv in baby_pokemon['individual_values']:
    if baby_pokemon['individual_values'][iv] is None:
        baby_pokemon['individual_values'][iv] = randint(1, 31)

print(baby_pokemon)
