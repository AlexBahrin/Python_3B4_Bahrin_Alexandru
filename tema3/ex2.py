def char_count(text):
    result = {}
    for char in text:
        result[char] = result.get(char, 0) + 1
    return result

print(char_count("Ana has apples."))