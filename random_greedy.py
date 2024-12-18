import save_load_json
import random


def random_greedy(capacity, group_max_items, items):
    # calculate ratios of items (item value / item weight)
    new_group_max_items = group_max_items.copy()
    ratios = []
    for i in range(len(items)):
        ratio = items[i]["value"] / items[i]["weight"]
        ratios.append([ratio, items[i]["weight"], items[i]["value"], items[i]["group"], items[i]["id"]])

    ratios.sort(reverse=True)
    actual_weight = 0
    overall_value = 0
    items_taken = []

    while ratios:
        top_3_candidates = ratios[:min(3, len(ratios))]
        chosen_item = random.choice(top_3_candidates)
        if (chosen_item[1] <= capacity - actual_weight) and new_group_max_items[chosen_item[3] - 1] > 0:
            items_taken.append(chosen_item)
            actual_weight += chosen_item[1]
            new_group_max_items[chosen_item[3] - 1] -= 1
            overall_value += chosen_item[2]
        ratios.remove(chosen_item)

    result_items = [item[4] for item in items_taken]

    return overall_value, result_items

#data = save_load_json.load_json_data("test.json")
#print(random_greedy(data[0], data[1], data[2]))