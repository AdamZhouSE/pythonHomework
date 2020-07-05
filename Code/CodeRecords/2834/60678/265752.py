nANDm = input().split()
n = int(nANDm[0])
m = int(nANDm[1])
answerA = []
answerB = []
answerC = []
answerD = []
answerE = []
answersOfStu = []
for i in range(0, n):
    answersOfStu.append(list(input()))
for questions in range(0, m):
    answerA.append(0)
    answerB.append(0)
    answerC.append(0)
    answerD.append(0)
    answerE.append(0)
    for students in range(0, n):
        if answersOfStu[students][questions] == 'A':
            answerA[questions] += 1
        elif answersOfStu[students][questions] == 'B':
            answerB[questions] += 1
        elif answersOfStu[students][questions] == 'C':
            answerC[questions] += 1
        elif answersOfStu[students][questions] == 'D':
            answerD[questions] += 1
        elif answersOfStu[students][questions] == 'E':
            answerE[questions] += 1

scores = input().split()
for i in range(0, len(scores)):
    scores[i] = int(scores[i])
sumScore = 0
for i in range(0, m):
    singleSum = max(answerA[i], answerB[i], answerC[i], answerD[i], answerE[i]) * scores[i]
    sumScore +=  singleSum
print(sumScore)