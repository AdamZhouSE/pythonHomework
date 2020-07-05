def s30():
    n = int(input())
    nums = list(input().split())
    m = 0

    for i in nums:
        if nums.count(i) > m:
            m = nums.count(i)

    print(m)

    
s30()
    