from math import gcd

def order_of_r_under_modulo(r, n):
    if gcd(r, n) != 1:
        return "not defined!"
    
    for k in range(1, n + 1):
        if pow(r, k, n) == 1: # r^k mod n
            return k
        
    return "not defined!"

r, n = map(int, input("Enter value of r and n: ").split())
print(f"{order_of_r_under_modulo(r, n)}")