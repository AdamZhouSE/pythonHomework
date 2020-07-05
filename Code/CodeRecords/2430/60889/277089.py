numOfInput = int(input())
for i in range(numOfInput):
    length = int(input())
    nums = input().split(" ")
    nums = list(map(int,nums))
    target = int(input())
    judge = True
    for j in range(len(nums)-1):
        for k in range(j+1,len(nums)):
            if nums[j]+nums[k]==target:
                judge = False
                print(nums[j],end=" ")
                print(nums[k],end=" ")
                print(target)
    if judge:
        print(-1)