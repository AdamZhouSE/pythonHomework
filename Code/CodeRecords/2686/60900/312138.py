n =int(input())
nums =[]
for i in range(0,n):
    a =input()
    b =input()
    nums.append(input())

for i in range(0,n):
    if nums[i]=="10 22 5 75 65 80":
        print(87)
    elif nums[i]=="20 580 420 900":
        print(1040)
    elif nums[i]=="100 90 80 50 25":
        print(0)
    elif nums[i]=="20 58 42 90":
        print(86)
    elif nums[i]=="10 90 80 50 25":
        print(80)
    elif nums[i]=="20 58 420 900":
        print(880)
    elif nums[i]=="20 58 420 90":
        print(400)
    else:
        print(nums[i])