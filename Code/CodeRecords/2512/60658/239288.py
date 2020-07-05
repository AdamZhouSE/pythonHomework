def mul(a,b,c):
    for i in range(a,b+1):
        li[i]*=c

def add(a,b,c):
    for i in range(a,b+1):
        li[i]+=c

def su(a,b):
    return sum(li[a:b+1])%p

n,p = [int(x) for x in input().split()]
li = [int(x) for x in input().split()]
m = int(input())
for i in range(m):
    s = [int(x) for x in input().split()]
    if s[0]==1:
        mul(s[1],s[2],s[3])
    elif s[0]==2:
        add(s[1],s[2],s[3])
    elif s[0]==3:
        print(su(s[1],s[2]))