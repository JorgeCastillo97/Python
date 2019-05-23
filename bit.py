print(5 >> 4)  # Right Shift
print(5 << 1)  # Left Shift
print(8 & 5)   # Bitwise AND
print(9 | 4)   # Bitwise OR
print(12 ^ 42) # Bitwise XOR
print(~88)     # Bitwise NOT
print(0b1 + 0b11)
print(0b11 * 0b11)

for b in range(1,5+1):
    print(bin(b))

"""When given a string containing a number and the base that number is in, 
the function will return the value of that number converted to base ten."""
print(int("0b11001001",2))