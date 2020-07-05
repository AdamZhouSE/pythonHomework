n,m=map(int,input().split())
num=list(map(int,input().split()))
for _ in range(m):
    i,j,k=map(int,input().split())
    temp=num[i-1:j]
    temp.sort(reverse=True)
    print(temp[-k])