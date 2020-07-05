t=int(input())
for ti in range(t):
    si=input().split(' ')
    n=int(si[0])
    k=si[1]
    s=input().split(' ')
    for i in range(n):
        if i+1==n:
            break
        lo=int(s[i])-int(k)
        hi=int(s[i+1])-int(k)
        if lo*hi <0:
            if hi+lo>0:
                print(s[i])
            else:
                print(s[i+1])
    #print(n,k,s)
    