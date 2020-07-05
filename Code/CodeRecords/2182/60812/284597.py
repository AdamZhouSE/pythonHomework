T = int(input())
for i in range(T):
    n, k = [int(i) for i in input().split(' ')]
    nums = [int(i) for i in range(1, n+1)]
    j, length = 0, n
    for i in range(n-1):
        j = (j+k-1)%length
        del nums[j]
        length -= 1
    print(nums[0])