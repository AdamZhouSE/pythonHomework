def change(a,b):
    li.append(tuple([a,b]))

def que(a,b):
    res = 0
    li.sort()
    for i in li:
        if i[0]<=b and i[1]>=a:
            res +=1
    return res

n,m = [int(x) for x in input().split()]
li = []
for i in range(m):
    s = [int(x) for x in input().split()]
    if s[0]==1:
        change(s[1],s[2])
    elif s[0]==2:
        print(que(s[1],s[2]))