a=int(input())
for i in range(0,a):
    b=int(input()[4])
    c=input().split(' ')
    for j in range(0,len(c)):
        c[j]=int(c[j])
    d=input().split(' ')
    for j in range(0,len(d)):
        d[j]=int(d[j])
    c.extend(d)
    c.sort()
    print(c[b-1])