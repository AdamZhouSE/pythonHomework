t = int(input())
for x in range(t):
    n = input()
    nums = input().split()
    count0 = 0
    count1 = 0
    count2 = 0
    for y in nums:
        if int(y) % 3 == 0:
            count0 += 1
        elif int(y) % 3 == 1:
            count1 += 1
        elif int(y) % 3 == 2:
            count2 += 1
    addcount = 0
    if count1 < count2:
        addcount = count1 + (count2 - count1) // 3
    else:
        addcount = count2 + (count1 - count2) // 3
    print(count0 + addcount)
