t=int(input())
while t>0:
    t=t-1
    n=int(input())
    s=input().split(' ')
    for i in range(0,n-1):
        for j in range(i+1,n):
            if int(s[i])>int(s[j]):
                s[i],s[j]=s[j],s[i]
    result=' '.join(s)
    print(result)