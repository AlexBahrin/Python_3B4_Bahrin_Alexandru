def fun(a,b,op:str):
    if op == 'intersected':
        new_list = []
        for element in a:
            if element in b:
                new_list.append(element)
        return new_list
    
    elif op == 'reunited':
        new_list=a
        for element in b:
            if not element in a:
                new_list.append(element)
        return new_list
    
    elif op == 'a-b':
        new_list = []
        for element in a:
            if not element in b:
                new_list.append(element)
        return new_list
    
    elif op == 'b-a':
        new_list = []
        for element in b:
            if not element in a:
                new_list.append(element)
        return new_list
    
    else: 
        return "Error"
    
result1 = fun([1,2,3,4],[3,4,5,6],'intersected')
print(result1)

result2 = fun([1,2,3,4],[3,4,5,6],'reunited')
print(result2)

result3 = fun([1,2,3,4],[3,4,5,6],'a-b')
print(result3)

result4 = fun([1,2,3,4],[3,4,5,6],'b-a')
print(result4)