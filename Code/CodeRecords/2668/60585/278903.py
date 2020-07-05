import math
t=eval(input())
for _ in range(t):
    n=eval(input())
    i=1
    a=1
    while a<n:
        i+=1
        a=round(math.pow(2,i))-1
    print(a-n,end=' ')
    print(a)