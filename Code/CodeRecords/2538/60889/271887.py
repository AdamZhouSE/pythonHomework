nums = input().strip("[]").split(",")
nums = list(map(int,nums))
for i in range(1,len(nums)+1):
    if nums.count(i)==0:
        print(i)
        break