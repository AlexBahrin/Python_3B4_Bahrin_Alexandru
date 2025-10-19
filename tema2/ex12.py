def group_by_rhyme(words):
    groups = {}
    
    for word in words:
        rhyme = word[-2:] if len(word) >= 2 else word
        if rhyme not in groups:
            groups[rhyme] = []
        groups[rhyme].append(word)
    
    return list(groups.values())


print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))