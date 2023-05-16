from random import randint
# used for calculating possible IV outcomes for Pokémon with 2 inputs, parent 1 and parent 2 (including items)
# example set dict {value: x, possibilities:{parent_1: x, parent_2: x, random: 'random'}}


def get_random_iv_to_set(ivs):
    ivs_left = []
    for iv in ivs:
        if ivs[iv]['value'] is None:
            ivs_left.append(iv)
    random_stat_index = randint(0, (len(ivs_left)-1))
    random_stat = ivs_left[random_stat_index]
    return random_stat


power_items = {'Power Weight': 'HP', 'Power Bracer': 'Attack', 'Power Belt': 'Defence', 'Power Lens': 'Special Attack',
               'Power Band': 'Special Defence', 'Power Anklet': 'Speed'}

# initialize list if IV's to get for baby
example_baby = {
    'individual_values': {
        'HP': {
            'value': None, 'possibilities': {
                'parent_1': {
                    'value': None, 'prob': None},
                'parent_2': {
                    'value': None, 'prob': None},
                'random': 'random'
            }
        },
        'Attack': {'value': None, 'possibilities': {'parent_1': {'value': None, 'prob': None}, 'parent_2': {'value': None, 'prob': None}, 'random': 'random'}},
        'Defence': {'value': None, 'possibilities': {'parent_1': {'value': None, 'prob': None}, 'parent_2': {'value': None, 'prob': None}, 'random': 'random'}},
        'Special Attack': {'value': None, 'possibilities': {'parent_1': {'value': None, 'prob': None}, 'parent_2': {'value': None, 'prob': None}, 'random': 'random'}},
        'Special Defence': {'value': None, 'possibilities': {'parent_1': {'value': None, 'prob': None}, 'parent_2': {'value': None, 'prob': None}, 'random': 'random'}},
        'Speed': {'value': None, 'possibilities': {'parent_1': {'value': None, 'prob': None}, 'parent_2': {'value': None, 'prob': None}, 'random': 'random'}},
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
    parent_stat2 = parent_2['individual_values'][item_stat]
    example_baby['individual_values'][item_stat]['value'] = parent_stat

    example_baby['individual_values'][item_stat]['possibilities']['parent_1']['value'] = parent_stat
    example_baby['individual_values'][item_stat]['possibilities']['parent_1']['prob'] = 100
    example_baby['individual_values'][item_stat]['possibilities']['parent_2']['value'] = parent_stat2
    example_baby['individual_values'][item_stat]['possibilities']['parent_2']['prob'] = 0
    example_baby['individual_values'][item_stat]['possibilities']['random'] = 0

    ivs_to_set = ivs_to_set - 1
elif parent_power_items > 0 and parent_power_inherit == 2:
    # inherit from parent_2
    parent_item = parent_2['held_item']
    item_stat = power_items[parent_item]
    parent_stat = parent_2['individual_values'][item_stat]
    parent_stat1 = parent_1['individual_values'][item_stat]
    example_baby['individual_values'][item_stat]['value'] = parent_stat

    example_baby['individual_values'][item_stat]['possibilities']['parent_1']['value'] = parent_stat1
    example_baby['individual_values'][item_stat]['possibilities']['parent_1']['prob'] = 0
    example_baby['individual_values'][item_stat]['possibilities']['parent_2']['value'] = parent_stat
    example_baby['individual_values'][item_stat]['possibilities']['parent_2']['prob'] = 100
    example_baby['individual_values'][item_stat]['possibilities']['random'] = 0

    ivs_to_set = ivs_to_set - 1


# inheriting IVs
for iv in range(ivs_to_set):
    # pick random iv
    stat_to_set = get_random_iv_to_set(example_baby['individual_values'])
    random_parent = randint(1, 2)

    if random_parent == 1:
        example_baby['individual_values'][stat_to_set]['value'] = parent_1['individual_values'][stat_to_set]
    else:
        example_baby['individual_values'][stat_to_set]['value'] = parent_2['individual_values'][stat_to_set]

    example_baby['individual_values'][stat_to_set]['possibilities']['parent_1']['value'] = parent_1['individual_values'][stat_to_set]
    example_baby['individual_values'][stat_to_set]['possibilities']['parent_1']['prob'] = 40
    example_baby['individual_values'][stat_to_set]['possibilities']['parent_2']['value'] = parent_2['individual_values'][stat_to_set]
    example_baby['individual_values'][stat_to_set]['possibilities']['parent_2']['prob'] = 40
    example_baby['individual_values'][stat_to_set]['possibilities']['random'] = 20

# setting leftover IVs
for iv in example_baby['individual_values']:
    if example_baby['individual_values'][iv]['value'] is None:
        example_baby['individual_values'][iv]['value'] = randint(1, 31)

        example_baby['individual_values'][iv]['possibilities']['parent_1']['value'] = parent_1['individual_values'][iv]
        example_baby['individual_values'][iv]['possibilities']['parent_1']['prob'] = 40
        example_baby['individual_values'][iv]['possibilities']['parent_2']['value'] = parent_2['individual_values'][iv]
        example_baby['individual_values'][iv]['possibilities']['parent_2']['prob'] = 40
        example_baby['individual_values'][iv]['possibilities']['random'] = 20

output = f'based on your input these are the possibilities and probabilities: \n'
for stat in example_baby['individual_values']:
    output += f'{stat}: {example_baby["individual_values"][stat]["value"]} ({example_baby["individual_values"][stat]["possibilities"]["parent_1"]["value"]}: {example_baby["individual_values"][stat]["possibilities"]["parent_1"]["prob"]}%, {example_baby["individual_values"][stat]["possibilities"]["parent_2"]["value"]}: {example_baby["individual_values"][stat]["possibilities"]["parent_2"]["prob"]}%, random: {example_baby["individual_values"][stat]["possibilities"]["random"]}%) \n'

print(output)
