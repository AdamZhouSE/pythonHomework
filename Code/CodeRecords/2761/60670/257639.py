t=int(input())
for k in range(0,t):
    n=int(input())
    total=0
    for i in range(0,n):
        total+=(n-i)**2
    print(total)