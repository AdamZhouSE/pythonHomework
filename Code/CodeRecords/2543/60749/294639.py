n=int(input())
ans=[]
for _ in range(n):
    k=int(input())
    ans.append(list(map(int, input().split(" "))))
def window(nums,k):
    ans=[]
    for t in range(0,len(nums)-k+1):
        temp=nums[t:t+k]
        minvalue=min(h for h in temp)
        ans.append(minvalue)
    return max(m for m in ans)
res=[]
for h in ans:
    temp=[]
    for t in range(1,len(h)+1):
        temp.append(window(h,t))
    res.append(temp)
for m in res:
    str1=str(m[0])
    if len(m)>1:
        for h in range(1,len(m)):
            str1=str1+" "+str(m[h])
    print(str1)

