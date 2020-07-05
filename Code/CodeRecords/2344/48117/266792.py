questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split(' ')
    d = int(input())

    ans = s[d:] + s[:d]
    for i in range(len(ans)):
        if i != len(ans) - 1:
            print(ans[i], end=' ')
        else:
            print(ans[i] + ' ')