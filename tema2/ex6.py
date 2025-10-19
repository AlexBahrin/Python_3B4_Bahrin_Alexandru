def fun(x,*l):
    dict={}
    for list in l:
        for elem in list:
            dict[elem] = dict.get(elem,0)+1
    
    for key in dict:
        if dict.get(key) == x:
            print(key,end=' ')

fun(2,[1,2,3,4],[2,3,4],[4,1,'test'])