def compare_dicts(d1, d2):
    if type(d1) != type(d2):
        return False

    if isinstance(d1, dict):
        if d1.keys() != d2.keys():
            return False
        for key in d1:
            if not compare_dicts(d1[key], d2[key]):
                return False
        return True

    elif isinstance(d1, (list, tuple)):
        if len(d1) != len(d2):
            return False
        for x, y in zip(d1, d2):
            if not compare_dicts(x, y):
                return False
        return True

    elif isinstance(d1, set):
        return d1 == d2

    else:
        return d1 == d2


a = {'x': 1, 'y': {'z': [1, 2, 3]}, 'w': {1, 2}}
b = {'x': 1, 'y': {'z': [1, 2, 3]}, 'w': {1, 2}}

print(compare_dicts(a, b))

c = {'x': 1, 'y': {'z': [1, 2, 4]}, 'w': {1, 2}}
print(compare_dicts(a, c))