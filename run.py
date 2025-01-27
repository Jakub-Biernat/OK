import save_load_json
import time
from random_greedy import random_greedy


def run(capacity, group_max_items, items, number_for_selection, run_time=180):
    start = time.time()
    best_overall_value = 0
    best_result_items = []
    number_of_results = 0

    while time.time() - start < run_time:
        overall_value, result_items = random_greedy(capacity, group_max_items, items, number_for_selection)
        number_of_results += 1
        if overall_value > best_overall_value:
            best_overall_value = overall_value
            best_result_items = result_items

    return best_overall_value, best_result_items, number_of_results

#data = save_load_json.load_json_data("test.json")
#print(run(data[0], data[1], data[2], 50, 5))