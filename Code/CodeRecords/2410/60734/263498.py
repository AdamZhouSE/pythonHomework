def find(lst,a,dif):
    if a in lst:
        return find(lst[lst.index(a)+1:],a+dif,dif)+1
    else:
        return 0
    
lst = list(map(int,input().split(',')))
dif = int(input())

max_s = 0
for i in range(len(lst)):
    a = lst[i]
    if a+dif in lst:
        max_s = max(max_s,1+find(lst[i+1:],a+dif,dif))
    else:
        max_s = max(max_s,1)