import math

def casual(n):
    if n<=4:
        return 0
    sum=0
    bound=int(math.log(5,n))+1
    for i in range(1,bound):
        sum+=(n//math.pow(5,i))
    return int(sum)


k=int(input())
i=0
sum=0
if k<0:
    print(0)
else:
    while casual(i)!=k:
    i+=1
    while casual(i)==k:
        sum+=1
        i+=1
    print(sum)