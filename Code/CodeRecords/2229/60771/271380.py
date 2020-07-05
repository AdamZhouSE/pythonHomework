#19
# 简单理解大概是：全局倒置不需要连续，局部需要？
ori = input().split(",")
nums = [int(item) for item in ori]
n = len(nums)
Acount = 0 #全局倒置
Bcount = 0 #局部倒置
for i in range(0,n):
    tar = nums[i]
    for j in range(i,n):
        if tar > nums[j]:
            Acount += 1
for i in range(0,n-1):
    if nums[i] > nums[i+1]:
        Bcount += 1
if Acount == Bcount:
    print(True)
else:
    print(False)