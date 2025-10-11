def bin_to_dec(n : str):
    p=0
    num=0
    while n!='0b':
        if n[-1] == '1':
            num+=pow(2,p)
        n=n[:-1]
        p+=1
    return num

def dec_to_hex(n:int):
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
    hex='0x'+hex
    print(hex)

def bin_to_hex(n):
    num=bin_to_dec(n)
    dec_to_hex(num)


bin_to_hex('0b1111110100')