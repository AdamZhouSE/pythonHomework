from itertools import combinations
def num(k,n):
    nums=[1,2,3,4,5,6,7,8,9]
    res=[]
    for i in range(len(nums)):
        res +=list(combinations(nums,i))
    res=[x for x in res if len(x) == k]
    a=[]
    for j in res:
        if sum(j) ==n :
            a.append(list(j))
    return a
k,n=int(i) for i in input().split(",")