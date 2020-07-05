def func(n):
    if n == 1:
        return 1
    else:
        x = n*(n+1)//2
        c = 1
        for i in range(n):
            c *= x
            x -= 1
        return c + func(n-1)
    
    
tests = int(input())
nums = []
for i in range(tests):
    nums.append(input())
for i in range(tests):
    print(func(int(nums[i])))
