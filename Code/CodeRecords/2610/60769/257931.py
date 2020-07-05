def getn(innum):
    return innum * (innum + 1) // 2


num = int(input())
for j in range(num):
    n = int(input())
    arr = input().split(" ")
    count = 1
    firstdup = 0
    for i in range(1, n):
        temp = arr[-i:]
        if arr[-1 - i] in temp:
            firstdup = max([firstdup, i - temp.index(arr[-1 - i])])
        count += getn(1 + i - firstdup)
    print(count)