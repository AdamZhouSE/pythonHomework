numStr = input().split(',')
count = 1
countList = []

for p1 in range(0, len(numStr)):
    for p2 in range(p1, len(numStr) - 1):
        if int(numStr[p2 + 1]) > int(numStr[p2]):
            count += 1

    countList.append(count)
    count = 1

print(max(countList))