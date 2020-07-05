nums = list(int(n) for n in input().split(','))
nums.sort()
k = 0
for i in nums:
    if i != k:
        print(k)
        break
    k += 1