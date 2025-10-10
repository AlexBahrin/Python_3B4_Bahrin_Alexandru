from math import gcd




nums = list(map(int, input("Enter numbers: ").split()))

result = nums[0]
for num in nums[1:]:
    result = gcd(result,num)

print(f"The gcd of these numbers is : {result}")