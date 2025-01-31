def isPrime(number):
    for i in range (2, (number//2) + 1):
        if number % i == 0: return False
        
    return True

def isMersenne(number): 
    for pow in range (2, number + 1):
        if number == (2 ** pow) - 1:
            return print(f"{number} is a Mersenne Number")
        
    return print(f"{number} is a Prime Number, but not a Mersenne Number")

num = int(input("Enter a Number: "))
if num <= 0: print("Enter a Number greater than 0")
else: isMersenne(num)
 

#3, 7, 31, 127, 8191, 131071, 524287, 2147483647