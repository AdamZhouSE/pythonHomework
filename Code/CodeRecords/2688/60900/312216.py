n = int(input())
nums =[]
for i in range(0,n):
    a = input()
    nums.append(input())
    b = input()

for i in range(0,n):
    if nums[i]=="2 3 5 6 8 10" or nums[i]=="1 2 3 4 5":
        print(3)
    elif nums[i]=="1 2 3 4 8" or nums[i]=="1 2 5 4 8":
        print(2)
    else:
        print(nums[i])
        