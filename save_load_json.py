import json


def save_json_file(problem, file_name):
    file = open(file_name, 'w')
    json.dump(problem, file, indent=5)


def load_json_data(jsonfile):
    file = open(jsonfile, 'r')
    data = json.load(file)
    capacity = data["capacity"]
    group_max_items = data["group_max_items"]
    items = data["items"]
    return capacity, group_max_items, items
