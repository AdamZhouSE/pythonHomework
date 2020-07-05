T=int(input())
for i in range(T):
    N=int(input())
    sum=0
    l=list(input().split())
    for item in l:
        for k in item:
            sum+=int(k)
    if sum%3==0:
        print(1)
    else:
        print(0)