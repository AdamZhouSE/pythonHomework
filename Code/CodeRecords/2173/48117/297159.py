questNum = int(input())

for quest in range(questNum):
    n = int(input())

    sum = 0
    for i in range(1, n + 1):
        start = 1
        for j in range(1, i + 1):
            sum += start
            start += 2
    
    print(sum)