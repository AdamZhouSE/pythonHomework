str1=input().split(", ")
nums=(str1[0])[8:-1]
nums=nums.split(",")
k=int((str1[1])[4:])
t=int((str1[2])[4:])
def judge(nums,k,t):
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if j-i<=k and abs(int(nums[i])-int(nums[j]))<=t:
                return True
    return False
if judge(nums,k,t):
    print("true")
else:
    print("false")
