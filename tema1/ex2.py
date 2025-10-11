string = input("Enter a string: ")

counter = 0
string=string.lower()
for letter in string:
    if letter=='a' or letter =='e' or letter=='i' or letter=='o' or letter=='u':
        counter+=1
print(counter)