s=input().split(" ")
n=int(s[0])
m=int(s[1])
nums=input().split(" ")
for i in range(n): nums[i]=int(nums[i])
step=[]
for i in range(m):
    list=input().split(" ")
    for j in range(3): list[j]=int(list[j])
    step.append(list)
q=int(input())

for i in range(len(step)):
    if step[i][0]==0:
        for j in range(step[i][1]-1,step[i][2]-1):
            for k in range(j+1,step[i][2]):
                if nums[j]>nums[k]:
                    temp=nums[k]
                    nums[k]=nums[j]
                    nums[j]=temp
    else:
        for j in range(step[i][1] - 1, step[i][2] - 1):
            for k in range(j + 1, step[i][2]):
                if nums[j] < nums[k]:
                    temp = nums[k]
                    nums[k] = nums[j]
                    nums[j] = temp
print(nums[q-1])
