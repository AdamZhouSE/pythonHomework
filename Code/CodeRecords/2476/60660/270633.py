t=int(input())
for i in range(t):
    n=int(input())
    l=eval('['+input().replace(' ',',')+']')
    l.sort()
    sum=0
    m=0
    while len(l)>=2:
        m=l[0]+l[1]
        sum+=l[0]+l[1]
        l.remove(l[0])
        l.remove(l[0])
        l.append(m)
        l.sort()
    print(sum)