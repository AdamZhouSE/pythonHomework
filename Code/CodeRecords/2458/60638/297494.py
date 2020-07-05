from itertools import combinations
def check(res):
    find=True
    for j in range(0,len(res[0])):
        find=True
        for i in range(1, len(res)):
            if not res[i].__contains__(res[0][j]):
                find=False
                break
        if find:
            break
    return find
nums=list(map(int,input().split(" ")))
length=nums[0]
n=nums[1]
numbers=[]
res=[]
for x in range(0,n):
    numbers.append(list(map(int,input().split(" "))))
for j in range(0,length):
    find=True
    res=[]
    for i in range(0,n):
        res.append(list(combinations(numbers[i],length-j)))
    for i in res[0]:
        find=True
        for k in range(1,n):
            if not res[k].__contains__(i):
                find=False
        if find:
            break
    if find:
        print(length-j)
        break