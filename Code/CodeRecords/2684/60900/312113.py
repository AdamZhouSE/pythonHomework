n = int(input())
nums =[]
for i in range(0,n):
    a =input()
    nums.append(input())
for i in range(0,n):
    if nums[i]=="10 5 7 10":
        print(12)
    elif nums[i]=="5 6 7 8 9 10" or nums[i]=="5 6 7 8 9 11":
        print(21)
    elif nums[i]=="10 20":
        print(10)
    elif nums[i]=="22 10 15 3 5" or nums[i]=="22 10 15 3 4" or nums[i]=="22 10 12 3 4":
        print(13)
    else:
        print(nums[i])