questNum = int(input())

for quest in range(questNum):
    n = int(input())
    base = 7
    start = 3
    ans = 0
    for i in range(n):
        ans = start
        start += base
        base += 4
    
    print(ans)