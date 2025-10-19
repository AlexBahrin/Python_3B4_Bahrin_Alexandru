def filter_chars(x=1, strings=[], flag=True):
    result = []
    for s in strings:
        if flag:
            filtered = [ch for ch in s if ord(ch) % x == 0]
        else:
            filtered = [ch for ch in s if ord(ch) % x != 0]
        result.append(filtered)
    return result


x = 2
strings = ["test", "hello", "lab002"]
flag = False

print(filter_chars(x, strings, flag))