def dec_to_bin(n):
    res=''
    while n>0:
        res = str(n%2) + res
        n//=2
    res = '0b'+res
    print(res)

dec_to_bin(8)
