def func(lis):
    ans=[]
    for i in range(0,len(lis)):
        temp=0
        for j in range(i-1,-1,-1):
            if lis[j]>=lis[i]:
                temp=temp+lis[i]
            else:
                break
        for j in range(i+1,len(lis)):
            if lis[j]>=lis[i]:
                temp=temp+lis[i]
            else:
                break
        ans.append(temp+lis[i])
    return max(ans)

n=int(input())
ans=[]
for i in range(0,n):
    input()
    s=list(map(int,input().split(" ")))
    ans.append(func(s))

for i in ans:
    print(i)