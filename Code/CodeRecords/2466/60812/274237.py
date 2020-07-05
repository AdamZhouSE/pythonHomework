T = int(input())
for i in range(T):
    n = int(input())
    if n < 3:
        print(0)
        continue
    nums = sorted(int(i) for i in input().split(' '))
    res = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if nums[k] < nums[i]+nums[j]:
                    res += 1
                else:
                    break
    print(res)