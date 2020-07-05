def isPowerOfTwo(n):
    if n == 1:
        return True
    elif n % 2 != 0:
        return False
    else:
        return isPowerOfTwo(n/2)


tests = int(input())
nums = []
for i in range(tests):
    nums.append(input())
for i in range(tests):
    n = int(nums[i])
    while not isPowerOfTwo(n):
        n += 1
    print(n)
