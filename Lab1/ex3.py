string1=input("Enter first string:")
string2=input("Enter second string:")

counter=0
pos=string1.find(string2)

while pos!=-1:
    counter+=1
    pos=string1.find(string2, pos + len(string2))

print(counter)