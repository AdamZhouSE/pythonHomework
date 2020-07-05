n = int(input())
nums =[]
cc = []
for i in range(0,n):
    nums.append(input().split(' '))
    for j in range(0,2):
        nums[i][j] = int(nums[i][j])

for i in range(0,n):
    c = []
    for j in range(nums[i][0]+1,nums[i][1]+1):
        c.append(j)
    cc.append(c)

result = 0
for i in range(0,n):
    listp=[]
    for j in range(0,n):
        if i ==j :
            continue
        else:
           listp = list(set(listp).union(set(cc[j])))
    result = max(result,len(listp))

print(result,end='')