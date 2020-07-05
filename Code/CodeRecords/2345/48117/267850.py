questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')
    
    for i in range(n):
        if s.count(s[i]) > 1:
            print(s[i])
            break