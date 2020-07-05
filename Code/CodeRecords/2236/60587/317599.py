n = int(input())
nums = []
for i in range(n):
    opt, num = input().split(' ')
    num = int(num)
    if opt == '1':
        nums.append(num)
    elif opt == '2':
        nums.remove(num)
    elif opt == '3':
        index = 0
        for j in range(len(nums)):
            if nums[j] == num:
                print(j + 1)
                break
    elif opt == '4':
        print(nums[num - 1])
    elif opt == '5':
        for j in range(1, len(nums)):
            if nums[j - 1] < num and nums[j] >= num:
                print(nums[j - 1])
                break
                
    else:
        for j in range(len(nums)):
            if num == nums[j]:
                print(nums[j+1])
                break
            elif num < nums[j]:
                print(nums[j])
                break
    nums.sort()
