questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')
    
    ans = '-1'
    for num in s:
        if s.count(num) % 2 != 0:
            ans = num
            break
    print(ans)