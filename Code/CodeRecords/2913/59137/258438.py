def s10():
    n = int(input())
    nums = list(input().split())
    count = 0
    
    for x in nums:
        count = count + int(x)
    
    if count % 2 == 1:
        print("NO")
    else:
        print("YES")


s10()