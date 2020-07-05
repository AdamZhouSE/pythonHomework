t=int(input())
nums=[]
for i in range(t):
    nums.append(list(map(int,input().split(' '))))
ans=[]
ans.append(nums[0])
for i in range(1,t):
    start = nums[i][0]
    end = nums[i][1]
    flag=True
    for j in range(len(ans)):
        prestart=ans[j][0]
        preend=ans[j][1]
        if(prestart<=start and start<=preend):
            ans[j][0] = min(prestart, start)
            ans[j][1] = max(end, preend)
            flag=False
            break
        elif(start<=prestart and prestart<=end):
            ans[j][0]=min(prestart,start)
            ans[j][1]=max(end,preend)
            flag=False
            break
    if(flag):
        ans.append(nums[i])
ans.sort(key=lambda x:x[0])
i=1
while i<len(ans):
    if(ans[i][0]<=ans[i-1][1]):
        ans[i-1][1]=max(ans[i-1][1],ans[i][1])
        ans.pop(i)
        i=i-1
    i=i+1
for j in ans:
    print(j[0],j[1])



