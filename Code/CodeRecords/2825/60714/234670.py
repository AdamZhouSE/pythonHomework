n = int(input())
scores = []
for i in range(0, n):
    scores.append(sum([int(x) for x in input().split()]))
myScore = scores[0]
scores.sort(reverse=True)
for i in range(0, n):
    if scores[i] is myScore:
        print(i + 1)
        break
