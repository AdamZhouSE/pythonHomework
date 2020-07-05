n=int(input())
nums=list(map(int, input().split(" ")))
def judgeTriangle(i,j,k):
    if i+j>k and i+k>j and j+k>i:
        return True
    return False
def judge(nums):
    for i in range(0,len(nums)-2):
        for j in range(i,len(nums)-1):
            for k in range(j, len(nums)):
                if judgeTriangle(nums[i],nums[k],nums[j]):
                    print("YES")
                    return
    print("NO")
    return
judge(nums)