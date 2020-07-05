t=int(input())
for i in range(t):
    n=int(input())
    l=eval('['+input().replace(' ',',')+']')
    l.sort()
    sum=1
    m=sum
    for i in range(n-1):
        if l[i+1]-l[i]!=1:
            m=max(sum,m)
            sum=1
        else:
            sum+=1
    print(m)