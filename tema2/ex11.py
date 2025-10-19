def sort_by_3rd_char(tuples_list):
    return sorted(tuples_list, key=lambda t: t[1][2] if len(t[1]) > 2 else "")


data = [('abc', 'bcd'), ('abc', 'zza')]
print(sort_by_3rd_char(data))