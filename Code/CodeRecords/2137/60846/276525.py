n=int(input())
divisor=[]
import math
for i in range(1,int(math.sqrt(n))+1):
    if n%i==0: 
        divisor.append(i)
        if i!=n/i and n/i!=n: divisor.append(n/i)
if sum(divisor)==n and n!=1: print("True")
else: print("False")    