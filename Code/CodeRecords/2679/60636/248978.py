t=int(input())
for i in range(t):
    n=int(input())
    print(int(n*(n-1)*(n-2)/2)+int(n*(n-1)/2)+int(n*(n-1))+2*n+1)