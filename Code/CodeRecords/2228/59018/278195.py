import math
def move(target):
    n=math.ceil(pow(2*target,1/2))
    num=sum([i for i in range(1,n+1)])
    while num<target or num-target%2!=0:
        n=n+1
        num=num+n
    print(n)    

target=int(input())
move(target)