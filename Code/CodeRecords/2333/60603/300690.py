import math

anslist=[]
x=int(input())
y=int(input())
bound=int(input())

for k in range(2,bound+1):
    for i in range(0,math.ceil(math.log(k,x))):
        if math.log(k-math.pow(x,i),y)%1==0:
            anslist.append(k)
            break
print(anslist)