t = int(input())
while t:
    l = int(input())
    nums = [int(n) for n in input().split( )]
    count = 0
    for i in range(l-1):
        for j in range(i+1, l):
            if nums[i]>nums[j]:
                count += 1
    print(count)
    t -= 1
    