import math
def smallnumber(N):
    num=int(math.pow(10,N))
    if N<=9:
        num=num*N
        return num
    else:
        count=0
        a=0
        while N>9:
            a=a+(9*math.pow(10,count))
            N=N-9
            count=count+1
        a=int(a+(N*math.pow(10,count)))
        num=num*a
        return num
    
    





T=int(input())
for i in range(T):
    N=int(input())
    print(smallnumber(N))