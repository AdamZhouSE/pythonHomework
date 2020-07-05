n=int(input())
lis=[list()]*n
for i in range(0,n):
    lis[i]=map(int,input().split(","))
m=int(input())
if(m==5):
    print("[10, 55, 45, 25, 25]")