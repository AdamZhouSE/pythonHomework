times = int(input())
for i in range(times):
    length = int(input())
    arrive = list(map(int, input().split(" ")))
    leave = list(map(int, input().split(" ")))
    current = 1
    Max = 1
    record = [[arrive[0],leave[0]]]
    for j in range(1, len(arrive)):
        for m in record:
            if arrive[j] >= m[1]:
                record.remove(m)
        record.append([arrive[j], leave[j]])
        Max = max(Max, len(record))
    print(Max)


