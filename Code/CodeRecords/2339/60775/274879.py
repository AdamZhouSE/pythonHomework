
T = int(input())

for t in range(T):
    size = int(input())
    nums = [int(x) for x in input().split(' ')]
    count = 0
    for i in range(size-1):
        for j in range(i+1,size):
            if nums[i] > nums[j]:
                count += 1
    print(count)