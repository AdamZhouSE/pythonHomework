t=int(input())
while t>0:
    t=t-1
    n,k=input().split(' ')
    n=int(n)
    k=int(k)
    s=input().split(' ')
    result=-1
    if k<=int(s[0]):
        result=int(s[0])
    else:
        for i in range(1,n):
            if int(s[i])<=k:
                continue
            else:
                if int(s[i])-k<=k-int(s[i-1]):
                    result=int(s[i])
                else:
                    result=int(s[i-1])
                break
    print(result)