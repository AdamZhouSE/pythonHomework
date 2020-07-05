import math
def happy(a):
    count=0
    tmp=a
    li=[]
    while(count!=1):
        li.append(tmp)
        count=0
        ass=str(tmp)
        for i in range(len(ass)):
            count+=int(math.pow(int(ass[i]),2))
        if count==1:
            return True
        else:
            if li.count(count)>0:
                return False
        tmp=count
t=int(input())
for i in range(t):
    n=int(input())
    while(True):
        n=n+1
        if happy(n):
            print(n)
            break
