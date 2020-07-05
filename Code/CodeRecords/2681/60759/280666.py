def findMin(num):
    if num in [0, 1, 2]:
        return num
    else:
        if num % 2:
            return 1 + findMin(num - 1)
        return 1 + findMin(num // 2)


ts = int(input())
for t in range(ts):
    n = int(input())
    print(findMin(n))
