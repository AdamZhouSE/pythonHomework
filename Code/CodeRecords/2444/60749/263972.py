str1=input().split(", ")
nums=(str1[0])[7:]
k=int((str1[1])[4:])
t=int((str1[2])[4:])
def judge(nums,k,t):
    for i in range(0,len(nums)-1):
        for j in range(i,len(nums)):
            if j-i<=k and abs(nums[i]-nums[j])<=t:
                return True
    return False
print(judge(nums,k,t))