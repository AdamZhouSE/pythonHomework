def findSquare(i, length):
    length = int(length)
    count = 0
    return (length - i) ** 2


times = int(input())

for loopTimes in range(0, times):
    length = int(input())
    count = 0
    for i in range(0, length):
        count += findSquare(i, length)
    print(count)