questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')
    d = int(input())
    
    ans = s[d:] + s[:d]
    print(ans)