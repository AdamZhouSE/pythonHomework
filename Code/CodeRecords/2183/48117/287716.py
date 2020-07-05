questNum = int(input())

for quest in range(questNum):
    line = int(input())

    end = 0
    start = 0
    for l in range(1, line + 1):
        end += l * 2
        start = end - (l * 2 - 1)

    sum = 0
    for i in range(start, end + 1):
        sum += i

    print(sum)