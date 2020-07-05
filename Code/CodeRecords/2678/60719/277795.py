nums = int(input())
for i in range(nums):
    n = int(input())
    i = 0
    while 2**i < n:
        i += 1
    if 2**i == n:
        print(i+1)
    else:
        print(-1)