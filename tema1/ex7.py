def count_bits(n: int) -> int:
    return bin(n).count("1")

print(count_bits(24)) 
print(count_bits(15))