n,m=map(int,input().split())
ans=[]
for i in range(n):
    ans.append(input())
scores=list(map(int,input().split()))
maxsum=0
for i in range(m):
    tmpstr=""
    tmpmax=0
    for j in range(n):
        tmpstr+=ans[j][i]
        tmpmax=max(tmpstr,key=tmpstr.count)
    maxsum+=(tmpstr.count(tmpmax))*scores[i]
print(maxsum)