str=input().split(" ")
n=int(str[0])
s=int(str[1])
nums=[]
for i in range(n):
    nums.append(int(input()))
res=[]
for i in range(n):
    end=len(nums)-1
    if end<=i:
        res.append(0)
        break
    if (end-i+1)%2==1:end-=1
    while 1:
        k1,k2=0,0
        for j in range(i,int(i+(end-i+1)/2)):k1+=nums[j]
        for j in range(int(i + (end - i + 1) / 2), end+1):k2+=nums[j]
        if k1<=s and k2<=s:
            res.append(end-i+1)
            break
        else:
            end-=2
for e in res:print(e)