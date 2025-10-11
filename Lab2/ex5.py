def verify(s:str):
    l=0
    r=0
    for c in s:
        if c=='(':
            l+=1
        if c==')':
            r+=1
    return l==r

print(verify('6+8*(5+3/2-1+6/(3+9)-7*(5+7/3))'))
print(verify("8-4*(3+7/8+4/(5-9)"))