n = int(input())
temp = [int(x) for x in input().split()]
medals = dict()
temp.sort()
for item in temp:
    if item in medals:
        medals[item] += 1
    else:
        medals[item] = 1
ans = 0
record = 0
for item in medals.keys():
    if medals[item] > 1:
        temp = medals[item] - 1
        i = max(item, record)
        while i in medals.keys() or temp > 0:
            if i not in medals.keys():
                ans = ans + i - item
                temp = temp - 1
            i += 1
        record = i
print(ans)
