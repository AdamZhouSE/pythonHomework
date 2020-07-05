nums = [int(i) for i in input().split(',')]
target = int(input())
try:
    print(nums.index(target))
except Exception as e:
    print(-1)