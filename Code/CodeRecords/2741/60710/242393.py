def solve(nums):
        
    count = 1
    m = 0
    if not nums:
        return 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            count += 1
        else:
            if count > m:
                m = count
            count = 1
    return max(m, count)

if __name__ == '__main__':
    num=eval(input())
    print(solve(num))
