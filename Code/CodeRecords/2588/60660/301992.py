import math
def is_prime(x):
    res=True
    for i in range(2,int(math.sqrt(x))+1):
         if x%i==0:
             res=False
    return res
def bitadd(x):
    sum=0
    while x>0:
        sum+=x%10
        x//=10
    return sum
def is_smith(x):
    i=2
    sum1=bitadd(x)
    sum2=0
    xx=x
    for i in range(2,xx):
        while x%i==0 and is_prime(i):
            sum2+=bitadd(i)
            x=x//i
    if sum2==sum1:
        return True
    else:
        return False
n=int(input())
for _ in range(n):
    x=int(input())
    if is_smith(x):
        print(1)
    else:
        print(0)