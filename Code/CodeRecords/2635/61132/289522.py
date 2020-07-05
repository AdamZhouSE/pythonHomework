import math

def casual(n):
    if n<=4:
        return 0
    sum=0
    bound=int(math.log(n,5))+1
    for i in range(1,bound):
        sum+=(n//math.pow(5,i))
    return int(sum)


k=int(input())
if k<0:
    print(0)
else:
    i = 0
    sum = 0
    while casual(i) <k:
        i += 1
    while casual(i) == k:
        sum += 1
        i += 1
    print(sum)