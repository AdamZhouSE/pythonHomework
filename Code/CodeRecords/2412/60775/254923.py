l1 = input().split(' ')
n = int(l1[0])
s = int(l1[1])
nums = [ int(i) for i in input().split(' ')]

def binary_sort(nums):
    copy = [i for i in nums]
    for i in range(1,len(copy)):
        L = 0
        R = i - 1
        M = (L + R) // 2
        p = M
        while True:
            if copy[M] < copy[i]:
                L = M + 1
                M = (L + R) // 2
            elif copy[M] > copy[i]:
                R = M - 1
                M = (L + R) // 2
            else:
                p = M
                break
            if R < L:
                p = L
                break
        copy.insert(p,copy.pop(i))
    return copy

def indexof(lis,n,visited):
    for i in range(len(lis)):
        if lis[i] == n and visited[i] == False:
            return i
    return 'error'

sorted = binary_sort(nums)
visited = [False for i in range(len(nums))]
result = []

for i in range(len(nums)):
    idx = i
    tmp = [idx+1]
    idx = sorted.index(nums[idx])
    while visited[idx] == False:
        tmp.append(idx+1)
        visited[idx] = True
        idx = indexof(sorted,nums[idx],visited)
        if tmp[-1] == tmp[0] and len(tmp)>1:
            break
    visited[i] = True
    if len(tmp)>1:
        result.append(tmp)

wait = []
for n in result:
    for m in n:
        if m not in wait:
            wait.append(m)

if (len(wait)>s or len(wait)==0) and (sorted != nums):
    print(-1)
elif sorted == nums:
    print(0)
else:
    print(1)
    print(len(wait))
    for i in range(len(wait)-1):
        print(str(wait[i]) + ' ',end='')
    print(str(wait[-1])+' ')
