t=int(input())
for time in range(0,t):
    s=input().split()
    n1=int(s[0])
    n2=int(s[1])
    n1=n1-1
    n2=n2-1
    sum1=n1+n2
    count=1
    for i in range(0,n1):
        count=count*(sum1-i)
    for j in range(1,n1+1):
        count=count//j
    print(count)