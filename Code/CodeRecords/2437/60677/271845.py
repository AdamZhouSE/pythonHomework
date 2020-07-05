axis=[0 for i in range(2*10000)]
i=10000
nums=input().split()
n=int(nums[0])
k=int(nums[1])
left=i
right=i
step=[]
for times in range(n):
    step=input().split()
    stepRange = int(step[0])
    if step[1]=="R":
        for j in range(i,i+stepRange):
            axis[j]+=1
        i=i+stepRange
        if i>right:
            right=i
    else:
        for j in range(i-stepRange,i):
            axis[j]+=1
        i=i-stepRange
        if i<left:
            left=i
fenceNums=0
for zzh in range(left,right):
    if axis[zzh]>=k:
        fenceNums+=1
print(fenceNums,end="")