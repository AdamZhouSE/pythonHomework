def sum(n):
    if n==1:
        return 1
    else:
        return int(n*(n+1)/2)
t= int(input())
for i in range(t):
    n=int(input())
    summary=0
    for i in range(1,n+1):
        summary+=sum(i)
    print(summary)