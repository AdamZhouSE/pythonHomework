from collections import deque
def findMaxAmongMin(nums,Nv):
    print(max(nums),end='')
    for i in range(Nv-1,0,-1):
        for j in range(0,i):
            nums[j]=min(nums[j],nums[j+1])
        nums.pop()
        print('',max(nums),end='')
    print()
t=int(input())
while t:
    Nv=int(input())
    line=[int(x) for x in input().split()]
    nums=deque(line)
    findMaxAmongMin(nums,Nv)
    t-=1