scores = {}
winner = ""
maxnum = -1
for h in range(int(input())):
    tem = input().split()
    if tem[0] not in scores:
        scores[tem[0]] = 0
    scores[tem[0]] = scores[tem[0]] + int(tem[1])
    if scores[tem[0]] > maxnum:
        winner = tem[0]
        maxnum = scores[tem[0]]
print(winner)
