from collections import Counter


t = int(input())
while t:
    l = int(input())
    nums = [int(n) for n in input().split( )]
    count = Counter(nums)
    for i in count:
        if count[i] % 2 == 1:
            print(i)
    t -= 1
    