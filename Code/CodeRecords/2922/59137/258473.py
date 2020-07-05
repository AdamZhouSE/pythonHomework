def s11():
    n = int(input())
    nums = list(input().split())
    for i in range(n):
        nums[i] = int(nums[i])

    li = list(set(nums))
    if len(li) > 3:
        print("NO")
    elif len(li) == 1:
        print("YES")
    elif len(li) == 2:
        if abs(li[0] - li[1]) % 2 != 0:
            print("NO")
        else:
            print("YES")
    else:
        arrange = (max(li) + min(li))/2
        if arrange % 1 != 0:
            print("NO")
        elif li.count(int(arrange)) == 0:
            print("NO")
        else:
            print("YES")


s11()