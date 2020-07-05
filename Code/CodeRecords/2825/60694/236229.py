num = int(input())

totalScore = []
for i in range(num):
    x = input()
    xlist = x.split(" ")
    scores = [int(xlist[i]) for i in range(len(xlist))]
    totalScore.append(sum(scores))

scoreOfSmith = totalScore[0]
totalScore.sort(reverse=True)

print(totalScore.index(scoreOfSmith) + 1)
