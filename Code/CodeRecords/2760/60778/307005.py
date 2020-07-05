UCs=int(input())
for UC in range(UCs):
    [n,money]=list(map(int,input().split()))
    print((n+1)//2*money)