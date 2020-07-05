import math
count=int(input())
for i in range(count):
    info=input().split()
    n=int(info[0])
    size=int(info[1])
    array = [int(x) for x in input().split()]
    nums=math.ceil(n/size)
    sub=[]
    curr=0
    ans=[]
    for j in range(nums):
        sub = array[curr:curr+size]
        for a in reversed(sub):
            ans.append(str(a))
        curr += size
    print(' '.join(ans), end=' \n')