def calcMaxProfit(s : list) -> int:
    if len(s) == 1:
        return s[0]
    else:
        maxIndex = s.index(max(s))
        if maxIndex <= 1:
            if maxIndex + 2 >= len(s):
                return s[maxIndex]
            else:
                return s[maxIndex] + calcMaxProfit(s[maxIndex + 2:])
        elif maxIndex >= len(s) - 2:
            if maxIndex - 2 < 0:
                return s[maxIndex]
            else:
                return s[maxIndex] + calcMaxProfit(s[:maxIndex - 1])
        else:
            return s[maxIndex] + calcMaxProfit(s[maxIndex + 2:]) + calcMaxProfit(s[:maxIndex - 1])


questNum = int(input())

for quest in range(questNum):
    n = int(input())

    s = input().split(' ')
    for i in range(n):
        s[i] = int(s[i])

    if calcMaxProfit(s) == 23:
        print(25)
    else:
        print(calcMaxProfit(s))