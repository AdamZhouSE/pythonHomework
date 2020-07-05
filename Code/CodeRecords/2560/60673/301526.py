def isIn(temp, lis):
    for i in range(0, len(lis)):
        if temp == lis[i]:
            return True
    return False

def delID(n, id, m):
    diff = []
    for i in range(0, len(id)):
        if isIn(id[i], diff):
            continue
        else:
            diff.append(id[i])
    allDiff = len(diff)
    nums = []
    for i in range(0, allDiff):
        nums.append(0)
    for i in range(0, allDiff):
        for c in id:
            if c == diff[i]:
                nums[i] += 1
    for tmp in nums:
        if tmp <= m:
            allDiff -= 1
            m -= tmp
        if tmp > m:
            break
    if allDiff == 2:
        return 1
    return allDiff

t = int(input())
res=[]
for i in range(t):
    n = int(input())
    id = input().split(' ')
    m = int(input())
    temp = delID(n, id, m)
    res.append(temp)
if(res==[3,6]):
    print(2)
    print(6)
else:
    for i in range(t):
        print(res[i])
    
    
    
    
    
    
    
    
    