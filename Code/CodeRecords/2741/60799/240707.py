aList = [int(i) for i in input().strip('[|]').split(',')]
current = max_num = 1
for i in range(1, len(aList)):
    if aList[i - 1] < aList[i]:
        current += 1
        max_num = max(max_num, current)
    else:
        current = 1
print(max_num)