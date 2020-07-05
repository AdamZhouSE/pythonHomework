def get(items):
    n=len(items)
    re=[]
    for i in range(2**n):
        combo = []
        for j in range(0,n):
            if (i>>j)%2:
                combo.append(items[j])
        re.append(combo)
    return re

t=int(input())
for ex in range(0,t):
    k=int(input())
    n=int(input())
    a=[int(i) for i in input().split()]
    temp=get(a)
    re=[]
    for i in temp:
        if len(i)<=2*k and len(i)%2==0:
            cur=0
            for j in range(0,len(i)):
                if j%2==0:
                    cur-=i[j]
                else:
                    cur+=i[j]
            re.append(cur)
    print(max(re))