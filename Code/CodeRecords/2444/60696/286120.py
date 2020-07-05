def solve(nums:list, k:int, t:int)->bool:
    for i in range(len(nums)-1):
        for j in range(i+1, i+k+1):
            if j < len(nums):
                if abs(nums[j] - nums[i]) <= t:
                    return True
    return False


if __name__ == '__main__':
    arr = input().split(', ')
    nums = [int(i) for i in str(arr[0][8:-1]).split(',')]
    k = int(str(arr[1]).split(' = ')[1])
    t = int(str(arr[2]).split(' = ')[1])
    if solve(nums, k, t):
        print('true')
    else:
        print('false')

