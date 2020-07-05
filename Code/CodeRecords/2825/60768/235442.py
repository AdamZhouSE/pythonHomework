students = int(input())

scores = []

smith = 1

for i in range(students):
    scores.append(input().split())
    scores[i] = [int(x) for x in scores[i]]
    scores[i] = scores[i][0] + scores[i][1] + scores[i][2] + scores[i][3]

for i in range(1, students):
    if scores[0] < scores[i]:
        smith = smith + 1

print(smith)