customers=eval("["+input()+"]")
grumpy=eval("["+input()+"]")
x=int(input())
maxt=0
lens=len(customers)
for i in range(x-1, lens):
    mid=0
    if (i>(x-1)):
        for a in range(0,i-x+1):
            if(grumpy[a]==0):
                mid=mid+customers[a]
    for b in range(i-x+1,i+1):
        mid=mid+customers[b]
    for c in range(i+1,lens):
        if(grumpy[c]==0):
            mid=mid+customers[c]
    if(mid>maxt):
        maxt=mid
print(maxt)