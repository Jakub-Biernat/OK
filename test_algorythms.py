import sys
import time

from generator import generate_problem
from brute_force import brute_force
from save_load_json import save_json_file, load_json_data
from greedy import greedy
from random_greedy import random_greedy


def test(capacity_range, value_range, group_range, items_number, json_file):
    problem = generate_problem(capacity_range, value_range, group_range, items_number)
    save_json_file(problem, json_file)
    data = load_json_data(json_file)


    start = time.time()
    greedy_result = greedy(data[0], data[1], data[2])
    end = time.time()
    print(greedy_result)
    print("Czas algorytmu zachłannego: ", round((end - start), 6))

    start = time.time()
    random_greedy_result = random_greedy(data[0], data[1], data[2])
    end = time.time()
    print(random_greedy_result)
    print("Czas algorytmu zachłannego ulosowionego: ", end - start)

    start = time.time()
    brute_result = brute_force(data[0], data[1], data[2])
    end = time.time()
    print(brute_result)
    print("Czas algorytmu siłowego: ", end - start)


if __name__ == "__main__":
    capacity_range = int(sys.argv[1])
    value_range = int(sys.argv[2])
    group_range = int(sys.argv[3])
    items_number = int(sys.argv[4])
    json_file = sys.argv[5]
    test(capacity_range, value_range, group_range, items_number, json_file)
