import math
def smallnumber(N):
    num=math.pow(10,N)
    if N<=9:
        num=num*N
    else:
        count=0
        a=0
        while N>9:
            a=a+(9*math.pow(10,count))
            N=N-9
            count=count+1
        a=a+(N*math.pow(10,count))
        num=num*a
    return (type(num))
    





T=int(input())
for i in range(T):
    N=int(input())
    print(smallnumber(N))