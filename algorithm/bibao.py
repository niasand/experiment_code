# coding: utf-8

import json
from functools import wraps
from log_lib import log


def voice(animal):
    def sound(voc):
        return sound


def add_print(func):
    def innner(*a, **b):
        return func(*a, **b)

    return innner


@add_print
def add(a, b):
    pass


def json_dumps_output(func):
    @wraps(func)
    def inner(*args, **kargs):

        result = func(*args, **kargs)
        return json.dumps(result)

    return inner


def json_out_put(indent=None, sort_keys=False):
    def json_dumps_func(func):
        @wraps(func)
        def inner(*args, **kargs):
            result = func(*args, **kargs)
            return json.dumps(result, indent=indent, sort_keys=sort_keys)
        return inner
    return json_dumps_func


@json_out_put(indent=4, sort_keys=True)
def no_json_dict():
    return {"d": "want to be json dumped", "c": "sorted or not?"}


def print_a():
    log.info("a")


def print_b():
    log.info("a")


def print_a_and_b(a_func, b_func):
    def add_print_hello(func):
        def inner(*args, **kargs):
            a = print_a()
            b = print_b()
            return a, b, func(*args, **kargs)

        return inner

    return add_print_hello


@print_a_and_b(print_a, print_b)
def get(a, b):
    log.info("a+b %s" % (a + b))


if __name__ == '__main__':
    '''
    wangcai : wangwang ..
    '''
    dog = voice("wangcai")

    add(1, 2)
    print(no_json_dict())
    get(1, 2)
