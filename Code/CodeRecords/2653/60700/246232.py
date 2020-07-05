tests = int(input())
nums = []
for i in range(tests):
    nums.append(input())
for i in range(tests):
    num = nums[i].split(' ')
    if int(num[1]) >= 10:
        print(0)
    else:
        print((int(num[0])-1)*(10-int(num[1])))
