n=int(input())

lis=list(map(int,input().split(" ")))

lis=sorted(lis)

ans=0
for i in range(0,len(lis),2):
    ans=lis[i+1]-lis[i]+ans

print(ans)