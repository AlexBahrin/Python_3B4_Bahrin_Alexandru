def revers(m):
    for i in range(0,len(m)):
        for j in range(0,len(m[i])):
            if j<i:
                m[i][j]=0
            print(m[i][j],end=' ')
        print()

revers([
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1]
    ])