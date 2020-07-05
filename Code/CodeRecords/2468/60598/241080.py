times = int(input())
for i in range(times):
    result = []
    size = int(input())
    nums = list(map(int, input().split(" ")))
    for j in range(len(nums)):
        product = 1
        for k in range(len(nums)):
            if k == j:
                pass
            else:
                product = product * nums[k]
        print(product,"",end="")
    print()