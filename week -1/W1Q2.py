x =(int)(input("Enter a Number : "))
sumC=0
z=x//2

for i in range(1,z+1):
    if(x % (i)== 0): sumC+=i;

if(sumC == x): print("perfect number");