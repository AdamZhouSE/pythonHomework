str1=input().split(",")
print(str1[0])
nums=(str1[0])[7:]
k=int(str1[1])
t=int(str1[2])
def judge(nums,k,t):
    for i in range(0,len(nums)-1):
        for j in range(i,len(nums)):
            if j-i<=k and abs(int(nums[i])-int(nums[j]))<=t:
                return True
    return False
print(judge(nums,k,t))