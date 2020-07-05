def s14():
    n = int(input())
    nums = list(input().split())
    x = nums.count('1')
    y = nums.count('2')
    count = min(x, y)
    
    if x - min(x, y) >= 3:
        count = count + int((x - min(x, y))//3)
    print(count)


s14()