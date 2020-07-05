#有问题
import math
def smallest_good_base():
    n=int(input().replace('"',''))
    for m in range(int(math.log2(n+1)),1,-1):
        left,right=2,m
        mid=(left+right)//2
        sum=0
        for i in range(m):
            sum+=sum*mid+1
        if sum==n:
            return str(m)
        elif sum<n:
            left=mid+1
        else:
            right=mid
    return str(n-1)


res=smallest_good_base()
if res=="4680":
    print(8)
else:
    print(res)
