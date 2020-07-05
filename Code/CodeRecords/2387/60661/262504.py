nm=input().split(' ')
n,m=int(nm[0]),int(nm[1])
nums=input().split(' ')
nums=[int(x) for x in nums]
op=[]
for i in range(m):
    op.append([int(x) for x in input().split(' ')])
for i in range(m):
    if op[i][0]==0:
        temp=sorted(nums[op[i][1]:op[i][2]])
        nums[op[i][1]:op[i][2]]=temp
    else:
        temp=sorted(nums[op[i][1]:op[i][2]])
        temp.reverse()
        nums[op[i][1]:op[i][2]]=temp
target=eval(input())
print(nums[target-1])