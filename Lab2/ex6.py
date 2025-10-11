def dec_to_hex(n):
    hex=''
    while n>0:
        if n%16==10:
            hex+='A'
        elif n%16==11:
            hex+='B'
        elif n%16==12:
            hex+='C'
        elif n%16==13:
            hex+='D'
        elif n%16==14:
            hex+='E'
        elif n%16==15:
            hex+='F'
        else:
            hex+=str(n%16)
        n//=16
    hex=hex[::-1]
    return hex

def string_converter(s:str):
    for word in s.split():
        p=''
        for c in word:
            p+=dec_to_hex(ord(c))
        print(p)

string_converter('abc 012')
