import save_load_json

def greedy(capacity, group_max_items, items, number_for_selection):
    # calculate ratios of items( item value/ item weight)
    new_group_max_items = group_max_items.copy()
    ratios = []
    for i in range(len(items)):
        ratio = items[i]["value"] / items[i]["weight"]
        ratios.append([ratio, items[i]["weight"], items[i]["value"], items[i]["group"], items[i]["id"]])

    new_ratios = []
    for i in range(min(number_for_selection, len(items))):
        new_ratios.append(max(ratios, key=lambda x: x[0]))
        ratios.remove(new_ratios[i])

    actual_weight = 0
    overall_value = 0
    items_taken = []
    for ratio in new_ratios:
        if (ratio[1] <= capacity - actual_weight) and new_group_max_items[ratio[3] - 1] > 0:
            items_taken.append(ratio)
            actual_weight += ratio[1]
            new_group_max_items[ratio[3] - 1] -= 1
            overall_value += ratio[2]

    result_items = []
    for i in range(len(items_taken)):
        result_items.append(items_taken[i][4])

    return overall_value, result_items


#data = save_load_json.load_json_data("test.json")
#print((greedy(data[0], data[1], data[2], 50)))