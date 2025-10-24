def count_unique_and_duplicates(lst):
    unique = set(lst)
    duplicates = len(lst) - len(unique)
    return (len(unique), duplicates)

print(count_unique_and_duplicates([1, 2, 2, 3, 4, 4, 4, 5]))