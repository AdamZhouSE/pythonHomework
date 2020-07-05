times=int(input())
for i in range(times):
    n=int(input())
    i=0
    while True:
        if n==0:
            break
        if n%2==0:
            n=n/2
            i=i+1
            continue
        if n%2==1:
            n=n-1
            i=i+1
            continue
    print(i)