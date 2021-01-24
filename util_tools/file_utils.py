# @Author: Zhiwei Yang
# @Date:   2021/1/24
import os
import json


def save_file_to_path(file_path, file_name, data):
    with open(file_path + file_name, "w") as f:
        f.write(data)


def read_file_from_path(file_path, file_name):
    with open(file_path + file_name, "r") as f:
        data = f.read()
    return data


def save_json_to_file(data, file_name, file_path):
    with open(file_path + file_name, "w+") as f:
        json.dump(data, f)


def read_api_json_to_file(file_name, file_path):
    with open(file_path + file_name, "r") as f:
        data = json.load(f)
    return data


def return_absoulte_path_from_home(path_point):
    return os.path.expanduser(f"~/{path_point}/")
