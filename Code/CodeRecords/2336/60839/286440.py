def func(lis,n):
    temp=[]
    ans=""
    for i in range(0,len(lis)-n+1):
        temp1=[]
        for j in range(i,i+n):
            temp1.append(lis[j])
        temp.append(max(temp1))
    ans=ans+str(temp[0])
    for i in range(1,len(lis)-n+1):
        ans=ans+" "+str(temp[i])
    return ans

n=int(input())
ans=[]
for i in range(0,n):
    m=int(input().split(" ")[1])
    s=list(map(int,input().split(" ")))
    ans.append(func(s,m))

for i in ans:
    print(i)
print("")