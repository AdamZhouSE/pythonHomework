questNum = int(input())

for quest in range(questNum):
    n = int(input())
    num = input().split(' ')
    k = int(input())
    for i in range(n):
        num[i] = int(num[i])

    ans = set()
    for i in range(n - 1):
        for j in range(i + 1, n):
            if abs(num[j] - num[i]) == k:
                ans.add((num[i], num[j]))
    
    print(len(ans))