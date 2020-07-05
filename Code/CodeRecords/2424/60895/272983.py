t=int(input())
while t>0:
    t=t-1
    n=int(input())
    s=input().split(' ')
    result=-1
    for i in range(0,n-1):
        for j in range(i+1,n):
            if int(s[i])>int(s[j]):
                s[i],s[j]=s[j],s[i]
    for k in range(1,n,2):
        if s[k]!=s[k-1]:
            result=int(s[k-1])
            break
    if result==-1:
        result=int(s[n-1])
    print(result)