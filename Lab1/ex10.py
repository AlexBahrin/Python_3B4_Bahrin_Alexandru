def count_words(text: str) -> int:
    if not text.strip():
        return 0
    return len(text.split(" "))

print(count_words("I have Python exam"))
print(count_words("Hello"))
print(count_words("This is a test"))
print(count_words(""))  