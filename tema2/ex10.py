def combine_lists(*lists):
    max_len = max(len(lst) for lst in lists)
    result = []

    for i in range(max_len):
        tuple_item = tuple(
            lst[i] if i < len(lst) else None
            for lst in lists
        )
        result.append(tuple_item)

    return result


a = [1, 2, 3]
b = [5, 6, 7]
c = ["a", "b", "c"]

print(combine_lists(a, b, c))