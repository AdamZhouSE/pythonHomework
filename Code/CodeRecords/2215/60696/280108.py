if __name__ == '__main__':
    nums = [int(i) for i in input().split(',')]
    for i in range(len(nums)):
        print(nums[i], end='')
        if i == 0 and len(nums)>2:
            print('/(',end='')
        elif i == len(nums)-1 and len(nums)>2:
            print(')',end='')
        elif len(nums) == 1:
            pass
        else:
            print('/',end='')
    print()