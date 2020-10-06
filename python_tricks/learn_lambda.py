#coding: utf-8


def map_lambda():
    l = ['foo', 'boo', 'bar']
    print(map(lambda x: x.upper(), l))


def filter_lambda():
    l = ['foo', 'boo', 'bar']
    print(filter(lambda x: 'f' in x, l))


def filter_map():
    l = ['foo', 'boo', 'bar']
    print(map(lambda x: x.upper(), filter(lambda y: 'f' in y, l)))


def sort_dict():
    students = [
        {'name': 'john', 'score': 'B', 'age': 15},
        {'name': 'jane', 'score': 'A', 'age': 12},
        {'name': 'dave', 'score': 'B', 'age': 10},
        {'name': 'ethan', 'score': 'C', 'age': 20},
        {'name': 'peter', 'score': 'B', 'age': 20},
        {'name': 'mike', 'score': 'C', 'age': 16}
    ]
    print(sorted(students, key=lambda x: x['age'], reverse=True))


def merge(x1, x2):
    if isinstance(x1, dict) and isinstance(x2, dict):
        res = x1.copy()
        for k, v in x2.items():
            res[k] = merge(res[k], v) if k in res else v
        return res
    elif isinstance(x1, list) and isinstance(x2, list):
        res = list(x1)
        res.extend(x2)
        return res
    elif x1 == x2:
        return x1
    else:
        raise ValueError(f"Cannot merge '{x1!r}' and '{x2!r}'")


if __name__ == '__main__':
    a = {"a": 1}
    b = {"s": 1}
    print(merge(a, b))
    map_lambda()
    filter_lambda()
    filter_map()
