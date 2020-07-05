def do(size,nums,k):
    if size == 1 or size == 0:
        return 0
    nums.sort()
    count = 0
    all = [(nums[0],nums[1])]
    if nums[1] - nums[0] == k:
        count += 1
    for i in range(size):
        for j in range(i+1,size):
            n1 = nums[i]
            n2 = nums[j]
            if n2 - n1 == k and (n1,n2) != all[-1]:
                all.append((n1,n2))
                count += 1
    return count



test = int(input())

for i in range(test):
    size = int(input())
    nums = [int(x) for x in input().split(' ')]
    k = int(input())
    print(do(size,nums,k))