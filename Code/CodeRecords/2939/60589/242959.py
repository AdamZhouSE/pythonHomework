km=input().split(' ')
K=int(km[0])
M=km[1] if km[1]!='' else km[2]
M=int(M)
s=set()
s.add(1)


def f(p,k):
    if k>0:
        s.add(2*p+1)
        s.add(4*p+5)
        f(2*p+1,k-1)
        f(4*p+5,k-1)


f(1,K)
s=list(s)
s.sort()
ans=''
for i in range(K):
    ans+=str(s[i])
print(ans)

ans=list(ans)
ans=list(map(int,ans))
ans2=''

left=0
right=M #在框中找最大值 当框当长度缩小到0时 就已经舍弃了M个数了 接下来每一个数都会加入结果（单个数最大就是自身）
maxx=0
n=len(ans)
while left <= right < n:
    for i in range(left,right+1):
        if ans[i]>maxx:
            maxx=ans[i]
            left=i+1
    ans2+=str(maxx)
    right=right+1
    maxx=0


print(ans2,end='')