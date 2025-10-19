from math import sqrt
def is_prime(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    return True

def check_list(l):
    new_list=[]
    for n in l:
        if is_prime(n):
            new_list.append(n)
    print(new_list)

check_list([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])