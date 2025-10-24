def loop(mapping):
    visited = set()
    result = []
    current = mapping["start"]

    while current not in visited:
        visited.add(current)
        result.append(current)
        current = mapping.get(current)
        if current is None:
            break

    return result

print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))