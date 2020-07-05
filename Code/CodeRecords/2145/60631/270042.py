def deo(sw):
    s=[]
    for i in sw:
        s.append(int(i))
    max=0
    max=len(s)*min(s)
    return max

t=int(input())
for ti in range(t):
    n=int(input())
    s=input().split(' ')
    li=[]
    for i in range(1,n+1):
        for j in range(n):
            a=s[j:j+i]
            if a not in li:
                li.append(a)
    max=0            
    for l in li:
        if deo(l) > max:
            max=deo(l)
    print(max)