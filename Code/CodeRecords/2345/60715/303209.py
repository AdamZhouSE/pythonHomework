def miss(num):
    ls=[]
    for i in range(1,len(num)+1):
        if i not in num:
             ls.append(i)
    if len(ls)==0:
        return 0
    return sorted(ls)[0]
def twice(num):
    ls=[]
    for i in range(len(num)-1):
        for j in range(i+1,len(num)):
            if num[i]==num[j]:
                ls.append(num[i])
    if len(ls)==0:
        return 0
    return sorted(ls)[0]
T=int(input())
while T>0:
    n=int(input())
    num=[int(n) for n in input().split()]
    print(twice(num),end=' ')
    print(miss(num))
    T-=1
