numOfInput = int(input())
for i in range(numOfInput):
    length = int(input())
    nums = input().split(" ")
    for i in range(len(nums)):
        if nums.count(nums[i]) != 1:
            print(i+1)
            break
    else:
        print(-1)