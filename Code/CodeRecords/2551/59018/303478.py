def change(a,b):
    for i in range(a-1,b):
        li[i]=0 if li[i]==1 else 1

def que(a,b):
    return sum(li[a-1:b])

n,m = [int(x) for x in input().split()]
li = [0]*n
for i in range(m):
    s = [int(x) for x in input().split()]
    if s[0]==0:
        change(s[1],s[2])
    elif s[0]==1:
        print(que(s[1],s[2]))