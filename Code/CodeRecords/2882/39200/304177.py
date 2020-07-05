n = int(input())
nums = input().split()
flag = 1
result = 1
for x in range(len(nums) - 1):
    if int(nums[x]) < int(nums[x+1]):
        if flag != 1:
            result = 0
            break
    elif int(nums[x]) == int(nums[x+1]):
        if flag == 1:
            flag = 2
        elif flag == 3:
            result = 0
            break
    else:
        if flag != 3:
            result = 0
            break
if result:
    print("YES")
else:
    print("NO")
