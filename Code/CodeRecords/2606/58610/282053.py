nums: list = eval(input())
i = eval(input())
try:
    print(nums.index(i))
except ValueError:
    print(-1)