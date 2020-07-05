length = int(input())
nums = input().split(" ")
nums = list(map(int,nums))
nums.sort()
for i in range(length-2):
    if nums[i]+nums[i+1]>nums[i+2]:
        print("YES")
        break
else:
    print("NO")