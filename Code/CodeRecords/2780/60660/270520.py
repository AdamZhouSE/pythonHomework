t=int(input())
for i in range(t):
    n=int(input())
    l=eval('['+input().replace(' ',',')+']')
    k=int(input())
    l.sort()
    sum=1
    for i in l:
        sum+=i
    print(sum%k)