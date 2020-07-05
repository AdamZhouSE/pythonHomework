numOfInput = int(input())
for i in range(numOfInput):
    length = int(input())
    nums = input().split(" ")
    nums = list(map(int,nums))
    target = int(input())
    judge = True
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                judge = False
                print(nums[i],end=" ")
                print(nums[j],end=" ")
                print(target)
    if judge:
        print(-1)