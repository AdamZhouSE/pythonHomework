t=int(input())
for ex in range(0,t):
    n=int(input())
    re=0
    while n>0:
        if n%2==1:
            n=n-1
            re+=1
        if n==0:
            break
        n=n//2
        re+=1
    print(re)