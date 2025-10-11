def is_vowel(c):
    c=c.lower()
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        return True
    return False

def fun(s:str):

    for word in s.split():
        print(word[0],word[-1],sep=' ')

    print()
    print()

    vocale=0
    consoane=0
    for c in s:
        if c.isalpha():
            if is_vowel(c):
                vocale+=1
            else:
                consoane+=1

    print(f"Avem {vocale} vocale")
    print(f"Avem {consoane} consoane\n\n")

    for word in s.split():
        print(word[::-1])
    count=0
    for c in s:
        if c.isupper():
            count+=1
    return count

print(fun("A fost de asemenea Remarcabil pentru Razboaiele persane si Pentru razboaiele Dintre orasele state Grecesti."))