def camel_to_snake(name: str) -> str:
    result = ""
    for i, ch in enumerate(name):
        if ch.isupper() and i != 0:
            result += "_"
        result += ch.lower()
    return result

string = input("Enter an UpperCamelCase string: ")
print("snake_case:", camel_to_snake(string))