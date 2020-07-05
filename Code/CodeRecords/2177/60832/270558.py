# 后缀排名数组 记录 后缀的排名


#  实际分析其 得来的方式！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！


k=int(input())

n=k+1

ans=n*['']

index=n-1-1
rank=1
while index>=0:
    ans[index]=rank
    rank+=1
    index-=2

if index==-2:
    index=1
else:       # index==-1
    index=0
while index<n:
    ans[index]=rank
    rank+=1
    index+=2

print(n)
for x in ans:
    print(x,end=' ')
