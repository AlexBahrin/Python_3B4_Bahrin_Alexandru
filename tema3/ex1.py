def list_set_operations(a, b):
    set_a = set(a)
    set_b = set(b)

    intersection = set_a & set_b
    union = set_a | set_b
    difference_a_b = set_a - set_b
    difference_b_a = set_b - set_a 

    return [intersection, union, difference_a_b, difference_b_a]

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

result = list_set_operations(a, b)
print(result)