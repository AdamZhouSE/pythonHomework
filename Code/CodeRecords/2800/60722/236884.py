string=input().split(" ")
n=int(string[0])
d=int(string[1])
nums=input().split(" ")
for i in range(n):
    nums[i]=int(nums[i])
time=0
for i in range(1,n):
    if nums[i]<=nums[i-1]:
        while nums[i]<=nums[i-1]:
            nums[i]+=d
            time+=1
print(time)