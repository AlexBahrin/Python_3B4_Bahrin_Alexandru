def fun(s:str,n:int):
    b = len(s)
    new_s=''
    while n>0:
        new_s+=s[n%b]
        n//=b
    new_s=new_s[::-1]
    print(new_s)

fun('abcd',301)
