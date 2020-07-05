import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:return True
    return False
t=eval(input())
for _ in range(t):    
    Range=list(map(int,input().strip().split(' ')))
    A=Range[0]
    B=Range[1]
    temp=A+B+1
    while isPrime(temp):
        temp+=1
    print(temp-A-B)
    