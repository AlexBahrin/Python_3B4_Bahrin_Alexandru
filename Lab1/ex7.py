def extract_number(text: str) -> int | None:
    num = ""
    for ch in text:
        if ch.isdigit():
            num += ch
        elif num: 
            break
    return int(num) if num else None


print(extract_number("An apple is 123 USD"))   
print(extract_number("abc123abc456"))             
print(extract_number("No digits here"))        