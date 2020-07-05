def x(c):
    res=[]
    for i in range(len(c)):
        res.append(c[i])
    res.sort()
    return res
n=int(input())
for i in range(n):
    count=0
    s=str(input())
    ss=x(str(input()))
    for j in range(0,len(s)-len(ss)+1):
        e=x(s[j:j+len(ss)])
        if e==ss:
            count += 1
    print(count)