t=int(input())
for i in range(t):
    n=int(input())
    a=input().split()
    for i in range(n):
        a[i]=int(a[i])
    b=input().split()
    for i in range(n):
        b[i]=int(b[i])
    c=input().split()
    for i in range(n):
        c[i]=int(c[i])
    count=0
    for i in range(n):
        for j in c:
            if a[i]==b[i]+j:
                count+=1
                break
    print(count)