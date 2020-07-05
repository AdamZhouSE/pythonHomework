m = int(input())

for i in range(m):
    n,k=map(int,input().split())
    print(pow(k,n-1,10**9+7))