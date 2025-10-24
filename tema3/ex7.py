def pairwise_set_operations(*sets):
    result = {}
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            a, b = sets[i], sets[j]
            result[f"{a} | {b}"] = a | b
            result[f"{a} & {b}"] = a & b
            result[f"{a} - {b}"] = a - b
            result[f"{b} - {a}"] = b - a
    return result

print(pairwise_set_operations({1, 2}, {2, 3}))