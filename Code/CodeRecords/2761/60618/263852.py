t=int(input())
for i in range(t):
    n=int(input())
    re=0
    for j in range(1,n+1):
        re+=(n//j+n%j)**2
    print(re)
        