n=int(input())
for I in range(n):
    l=int(input())
    s=input().split()
    for i in range(l):
        s[i]=int(s[i])
    s.sort()
    res=s[-1]*s[-2]*s[-3]
    print(res)