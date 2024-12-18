import save_load_json
import itertools


def brute_force(capacity, group_max_items, items):
    max_value = 0
    max_items = []

    for option in itertools.product([0, 1], repeat= len(items)):
        actual_value = 0
        actual_weight = 0
        actual_group = [0] * len(group_max_items)
        for i in range(len(option)):
            if option[i] == 1:
                actual_value += items[i]["value"]
                actual_weight += items[i]["weight"]
                actual_group[items[i]["group"] - 1] += 1

        proper = True
        if actual_value > max_value and actual_weight <= capacity:
            for i in range(len(group_max_items)):
                if group_max_items[i] < actual_group[i]:
                    proper = False
                    break
            if proper:
                max_value = actual_value
                max_items = option

    result_items = []
    for i in range(len(max_items)):
        if max_items[i] == 1:
            result_items.append(i)

    return max_value, result_items

#data = save_load_json.load_json_data("test.json")
#print(brute_force(data[0], data[1], data[2]))