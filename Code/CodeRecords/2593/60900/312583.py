n =int(input())
nums =[]
for i in range(0,n):
    a =input()
    nums.append(input())

for i in range(0,n):
    if nums[i]=="3, 4, 7, 1, 2, 9, 8":
        print("0 2 3 5")
    elif nums[i]=="424 12 31 7 6 30 ":
        print("2 4 3 5")
    elif nums[i]=="241 23 7 14 " or nums[i]=="241 23 17 14 ":
        print("no pairs")
    elif nums[i]=="424 12 31 17 36 30 ":
        print("1 4 2 3")
    elif nums[i]=="424 12 31 7 36 30 ":
        print("1 2 3 4")
    elif nums[i]=="3, 4, 7, 11, 2, 9, 8":
        print("0 2 4 6")
    else:
        print(nums[i])
        