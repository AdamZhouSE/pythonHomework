t=int(input())
while t>0:
    t=t-1
    n=int(input())
    s=input().split(' ')
    for i in range(1,n,2):
        s[i],s[i-1]=s[i-1],s[i]
    result=' '.join(s)
    print(result)