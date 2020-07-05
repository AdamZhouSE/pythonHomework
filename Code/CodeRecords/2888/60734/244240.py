def inquiry(a):
    section = a[1]-a[0]+1
    if section%2 == 0:
        if lst.count(-1)>=section/2 and lst.count(1)>=section/2:
            return 1
    return 0
    
lst = input().split(' ')
n = int(lst[0])
m = int(lst[1])
lst = list(map(int,input().split()))
res = []

for i in range(m):
    res.append(inquiry(list(map(int,input().split()))))

for x in res:
    print(x)