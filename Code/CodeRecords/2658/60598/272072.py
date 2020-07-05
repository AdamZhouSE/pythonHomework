times = int(input())
for i in range(times):
    x = int(input().split(" ")[1])
    nums = list(map(int, input().split(" ")))
    result = 0
    for num in nums:
        if num % x == 0:
            result |= num
    print(result)

    