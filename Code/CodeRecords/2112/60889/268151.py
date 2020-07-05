nums = input().split(",")
nums = list(map(int,nums))
for i in range(len(nums)+1):
    if nums.count(i)==0:
        print(i)
        break