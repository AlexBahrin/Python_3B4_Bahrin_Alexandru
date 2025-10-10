def most_common_letter(text: str):
    counts = {}
    for ch in text.lower():
        if 'a' <= ch <= 'z':
            counts[ch] = counts.get(ch, 0) + 1

    if not counts:
        return None, 0 

    max_letter = None
    max_count = 0
    for letter, count in counts.items():
        if count > max_count:
            max_letter = letter
            max_count = count

    return max_letter, max_count


s = "an apple is not a tomato"
letter, count = most_common_letter(s)
print(f"The most common letter is '{letter}' ({count} times).")