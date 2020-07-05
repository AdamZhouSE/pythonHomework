questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')
    for i in range(n):
        s[i] = int(s[i])

    ans = 1
    for j in range(3):
        ans *= max(s)
        del s[s.index(max(s))]
    
    print(ans)