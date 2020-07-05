n=int(input())
lis=[]
for i in range(0,n):
    lis.append(list(map(int,input().split(","))))
sum=int(input())
ans=[]
for i in range(0,sum):
    ans.append(0)
for iterm in lis:
    for i in range(iterm[0]-1,iterm[1]):
        ans[i]+=iterm[2]
print(ans)         