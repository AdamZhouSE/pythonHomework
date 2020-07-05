def func(lis):
    n=lis[0]//2
    if lis[0]%2==0:
        return n*lis[1]
    else:
        return (n+1)*lis[1]


n=int(input())
ans=[]
for i in range(0,n):
    s=list(map(int,input().split(" ")))
    ans.append(func(s))

for i in ans:
    print(i)