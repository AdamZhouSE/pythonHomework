times = int(input())
for loopTimes in range(0, times):
    length = int(input())
    things = input().split()
    overall = 0

    while len(things) > 0:
        tempCmp = things[0]
        count = 0
        index = 0
        while index < len(things):
            if things[index] == tempCmp:
                count += 1
                del things[index]
                index -= 1
            index += 1
        overall += count // 2
        count = 0
    print(overall * 2)