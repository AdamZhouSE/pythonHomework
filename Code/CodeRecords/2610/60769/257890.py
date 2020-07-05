def getn(innum):
    return innum * (innum + 1) // 2


num = int(input())
for j in range(num):
    n = int(input())
    arr = input().split(" ")
    count = 1
    for i in range(1, n):
        temp = arr[-i:]
        if arr[-1 - i] in temp:
            count += getn(temp.index(arr[-1 - i]) + 1)
        else:
            count += getn(1 + i)
    print(count)
    if count == 8:
        print(arr)