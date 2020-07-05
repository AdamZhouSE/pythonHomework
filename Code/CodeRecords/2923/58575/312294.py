temp=input().split(" ")
n=int(temp[0])
q=int(temp[1])

nums=list(map(int,input().split(" ")))
nums.sort()

times={}

ques=[]
for i in range(q):
    temp=list(map(int,input().split()))
    j=temp[0]
    while j<=temp[1]:
        if j not in times:
            times[j]=1
        else:
            times[j]+=1
        j+=1
times=dict(sorted(times.items(),key=lambda x:x[1],reverse=True))
sum=0
for i in times:
    maxNum=max(nums)
    index=nums.index(maxNum)
    sum+=times[i]*maxNum
    nums=nums[0:index]+nums[index+1:]
print(sum)