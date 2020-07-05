def s2():
    s = input().split()
    n = int(s[0])
    k = int(s[1])
    nums = list(input().split())

    index1 = index2 = -1
    for i in range(n):
        if int(nums[i]) > k:
            index1 = i
            break
    for j in range(n):
        if int(nums[n-j-1]) > k:
            index2 = n-j-1
            break

    if index1 == -1 and index2 == -1:
        print(n)
    else:
        print(n - index2 + index1 - 1)


s2()