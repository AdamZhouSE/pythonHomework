import math

def isPerfectSquareNumber(x):
    return math.floor(math.sqrt(x))**2 == x

def isvalid(lst):
    for i in range(1,len(lst)):
        if isPerfectSquareNumber(lst[i]+lst[i-1]) == False:
            return False
    return True

def perm(lst,position,end):
    if position == end:
        lst_copy = lst.copy()
        if lst_copy not in alls:
            alls.append(lst_copy)
    else:
        for i in range(position,end):
            lst[i],lst[position] = lst[position],lst[i]
            perm(lst,position+1,end)
            lst[i],lst[position] = lst[position],lst[i]

lst = list(map(int,input().split(',')))
alls = []
perm(lst,0,len(lst))
res = []
for x in alls:
    if isvalid(x):
        res.append(x)
print(len(res))