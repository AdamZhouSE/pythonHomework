t=int(input())
while t>0:
    t=t-1
    n=int(input())
    s=input().split(' ')
    index=0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if int(s[i])>int(s[j]):
                s[i],s[j]=s[j],s[i]
    for k in range(0,n-1):
        if s[k]==s[k+1]:
            print(int(s[k]),end=' ')
            index=index+1
            break
    for m in range(0,n):
        if int(s[m])!=(m+1):
            print(m+1)
            break
    if index==0:
        print(0,end=' ')
        print(0)