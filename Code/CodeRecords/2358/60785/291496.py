t=int(input())
for dd in range(t):
    n,k=[int(i)  for i in input().split()]
    nums=[int(i)  for i in input().split()]
    nums.sort()
    nums.reverse()
    res=nums[0:k]
    res=[str(i) for i in res]
    print(' '.join(res),end=' ')
    print()