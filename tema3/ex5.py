def validate_dict(rules, d):
    for key, prefix, middle, suffix in rules:
        if key not in d:
            return False
        value = d[key]
        if not value.startswith(prefix):
            return False
        if not value.endswith(suffix):
            return False
        if middle not in value[len(prefix):len(value)-len(suffix) if suffix else None]:
            return False

    if len(rules) != len(d):
        return False

    return True

s = {
    ("key1", "", "inside", ""),
    ("key2", "start", "middle", "winter")
}
d = {
    "key1": "come inside, it's too cold out",
    "key3": "this is not valid"
}

print(validate_dict(s, d))