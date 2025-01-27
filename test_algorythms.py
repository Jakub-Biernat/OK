import sys
import time

from generator import generate_problem
from brute_force import brute_force
from save_load_json import save_json_file, load_json_data
from greedy import greedy
from random_greedy import random_greedy
from run import run


def test(capacity_range, value_range, group_range, items_number, number_for_selection, run_time, json_file):
    problem = generate_problem(capacity_range, value_range, group_range, items_number)
    save_json_file(problem, json_file)
    data = load_json_data(json_file)


    start = time.time()
    greedy_result = greedy(data[0], data[1], data[2], number_for_selection)
    end = time.time()
    print(greedy_result)
    print("Czas algorytmu zachłannego: ", round((end - start), 6))

    start = time.time()
    random_greedy_result = random_greedy(data[0], data[1], data[2], number_for_selection)
    end = time.time()
    print(random_greedy_result)
    print("Czas algorytmu zachłannego ulosowionego: ", round((end - start), 6))

    start = time.time()
    brute_result = brute_force(data[0], data[1], data[2])
    end = time.time()
    print(brute_result)
    print("Czas algorytmu siłowego: ", round((end - start), 6))

    run_result = run(data[0], data[1], data[2], number_for_selection, run_time)
    print((run_result[0], run_result[1]))
    print("Ilosc wygenerowanych rezultatów: ", run_result[2])

if __name__ == "__main__":
    capacity_range = int(sys.argv[1])
    value_range = int(sys.argv[2])
    group_range = int(sys.argv[3])
    items_number = int(sys.argv[4])
    number_for_selection = int(sys.argv[5])
    run_time = int(sys.argv[6])
    json_file = sys.argv[7]
    test(capacity_range, value_range, group_range, items_number, number_for_selection, run_time, json_file)
