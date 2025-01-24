def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p

x =(int)(input("Enter a Number : "))
y =(int)(input("Enter a Number : "))
print(gcd(x, y))
