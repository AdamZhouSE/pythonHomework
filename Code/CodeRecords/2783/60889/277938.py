numOfInput = int(input())
scores = {}
maxScore = 0
for i in range(numOfInput):
    score = input().split(" ")
    lastRoundScore = scores.get(score[0],0)
    nowScore = lastRoundScore + int(score[1])
    if nowScore > maxScore:
        maxScore = nowScore
        firstReach = score[0]
    scores[score[0]] = nowScore
print(firstReach)