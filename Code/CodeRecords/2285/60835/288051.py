for q in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    res = []
    x = 1
    while x < n:
        if nums[x] > nums[x - 1]:
            start = x - 1
            end = 0
            while True:
                if x == n - 1:
                    end = x
                    break
                if nums[x] < nums[x - 1]:
                    end = x - 1
                    break
                x = x + 1
            res.append([start,end])
        x = x + 1
    for x in res:
        if x != res[0]:
            print(" ", end = "")
        print("(" + str(x[0]) +" " + str(x[1]) + ")", end = "")
    print()