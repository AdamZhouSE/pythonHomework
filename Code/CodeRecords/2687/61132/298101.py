import math

def jiaoti():
    n=1
    while True:
        tmp=n
        Sum=0
        while tmp>=0:
            Sum+=math.pow(2,tmp)
            tmp-=2
        yield Sum
        n+=1


t = int(input())
for j in range(t):
    k=int(input())
    ans=[]
    for i in jiaoti():
        if i >k:break
        ans.append(str(int(i)))
    print(' '.join(ans))