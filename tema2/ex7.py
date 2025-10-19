def palindrome_info(numbers):
    palindromes = [n for n in numbers if str(n) == str(n)[::-1]]
    
    if palindromes:
        count = len(palindromes)
        greatest = max(palindromes)
    else:
        count = 0
        greatest = None
    
    return (count, greatest)


result = palindrome_info([121, 34, 22, 454, 12321, 78])
print(result)