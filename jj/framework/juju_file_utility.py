import os.path
import json
from typing import IO

initial_path = "./"


def path_builder(*paths: str):
    return str(paths).replace('\'', '').replace('(', '').replace(')', '').replace(', ', os.sep)


def jj_path_builder(*paths: str):
    return path_builder(initial_path, str(paths))


def jj_create_file(path: str, name: str):
    a: IO = open(initial_path + path + name, 'r')

    if not os.path.exists(jj_path_builder(path, name)):
        a = open(initial_path + path + name, 'w')
    return a


def jj_read_file(path: str, name: str):
    a = open(path_builder(initial_path, path, name), 'r')
    str_line = ""

    while True:
        line = a.readline()
        if not line:
            break
        str_line += line

    a.close()
    return str_line


def jj_write_file(path: str, name: str, data=''):
    a = open(path_builder(initial_path, path, name), 'w')
    if type(data) != str:
        data = str(data)
    a.write(data)
    return a


def jj_file_contains(path: str, name: str, obj):  # Answers file contains the thing
    return list(jj_read_file(path, name)).__contains__(obj)


def jj_is_there_folder(path: str, name: str):  # Finds out file
    return os.path.exists(jj_path_builder(path, name))


# Creates certain folder if there is no such.
# and returns True if its created.
def jj_create_folder_if_can(path: str, name: str):
    t = False

    if not jj_is_there_folder(path, name):
        t = True
        os.makedirs(jj_path_builder(path, name))

    return t


mini_repo_path: str = "mini_data/"


class jj_mini_repository:
    def __init__(self, pickup_file=None):
        self.data_file = pickup_file
        self.data: dict = dict()

        pass

    def set_file_name(self, name):
        self.data_file = name
        return self

    def setup_data_file(self, name=None):
        if name is None:
            name = self.data_file
        if name is None:
            print("Error: No name found in object. please suggest the name.")

        jj_create_folder_if_can("", "mini_data")
        f = jj_create_file(mini_repo_path, name)
        if f.writable():
            f.write("{}")
            pass
        f.close()
        self.set_file_name(name)
        return self

    def add_data(self, key, value):
        self.data[key] = value
        return self

    def push(self):
        jj_write_file(mini_repo_path, self.data_file, json.dumps(self.data)).close()

        return self

    def pull(self):
        the_data: dict = {}

        try:
            the_data = json.loads(jj_read_file(mini_repo_path, self.data_file))
        except FileNotFoundError:
            print("Error: There is no file to read. please make data file first.")

        self.data = the_data

        return self

    def get_data(self) -> dict:
        return self.data

    def pop_data(self, key):
        self.data.pop(key)
        return self
