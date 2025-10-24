def count_common_values(*args, **kwargs):
    return sum(1 for x in args if x in kwargs.values())

print(count_common_values(1, 2, 3, 4, x=1, y=2, z=3, w=5))