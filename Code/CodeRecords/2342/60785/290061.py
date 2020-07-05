t =int(input())
for te in range(t):
    n,k=[int(i) for i in input().split()]
    nums = input().split()
    x=n//k
    res=[]
    for i in range(n):
        tmp=nums[k*i:k*i+k]
        tmp.reverse()
        res+=tmp
    print(' '.join(res),end=' ')
    print()
        