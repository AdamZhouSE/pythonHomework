t=int(input())
for i in range(t):
    n=int(input())
    l=eval('['+input().replace(' ',',')+']')
    l.sort()
    if len(l)%2==0:
        result=str((l[n//2-1]+l[n//2])//2)
        print(result)
    else:
        print(l[n//2])