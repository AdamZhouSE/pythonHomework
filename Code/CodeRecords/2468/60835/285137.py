for r in range(int(input())):
    n = int(input())
    tem = input().split()
    nums = []
    for a in tem:
        nums.append(int(a))
    res = []
    for x in nums:
        tem = 1
        for y in nums:
            if y != x:
                tem = tem * y
        res.append(tem)
    for x in res:
        print(x,end = " ")
    print()