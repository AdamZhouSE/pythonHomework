tests = int(input())
nums = []
for i in range(tests):
    nums.append(input())
for i in range(tests):
    num = nums[i].split(' ')
    if int(num[0]) > int(num[1])*(int(num[1])+1)/2:
        print('1')
    else:
        print('0')
