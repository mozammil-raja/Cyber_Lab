def isPowerOf2K(n):
    return n & (n - 1 )  == 0

n = int(input("Enter a Number: "))

if n <= 0: print("Enter a Number greater than 0")
else: print(isPowerOf2K(n))
