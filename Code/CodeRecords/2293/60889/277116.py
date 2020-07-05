numOfInput = int(input())
for i in range(numOfInput):
    length = int(input())
    nums = input().split(" ")
    nums = list(map(int,nums))
    loc = int(input())
    nums.sort()
    print(nums[loc-1])