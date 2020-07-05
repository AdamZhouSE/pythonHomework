nm=input().split(' ')
n,m=int(nm[0]),int(nm[1])
nums=input().split(' ')
nums=[int(x) for x in nums]
op=[]
for i in range(m):
    op.append([int(x) for x in input().split(' ')])
    if op[i][0]==0:
        nums[op[i][1]:op[i][2]+1].sort()
    else:
        nums[op[i][1]:op[i][2]+1].sort()
        nums[op[i][1]:op[i][2]+1].reverse()
target=eval(input())
print(nums[target])