import random


def generate_problem(capacity_range, value_range, group_range, items_number):

    item_list = []
    for i in range(items_number):
        item = {
            "id": i,
            "value": random.randint(1, value_range),
            "weight": random.randint(1, capacity_range),
            "group": random.randint(1, group_range)
        }
        item_list.append(item)

    group_max_items = []
    for _ in range(group_range):
        group_max_items.append(random.randint(0, items_number))

    problem = {
        "capacity": random.randint(1, capacity_range),
        "group_max_items": group_max_items,
        "items": item_list
    }

    return problem
