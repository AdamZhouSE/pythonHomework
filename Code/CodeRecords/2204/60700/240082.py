def prints(n):
    if n > 0:
        prints(n - 1)
        print(n, end=' ')


tests = int(input())
nums = []
for i in range(tests):
    nums.append(input())
for i in range(tests):
    prints(int(nums[i]))
    print()
