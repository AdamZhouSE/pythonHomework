s = list(input().split())
n = int(s[0])
m = int(s[1])
s = []
score = 0
choice = ['A', 'B', 'C', 'D', 'E']
for i in range(n):
    s.append(list(input()))
points = list(map(int, input().split()))
for i in range(m):
    OneQuestion = []
    for j in range(n):
        OneQuestion.append(s[j][i])
    temp = []
    for ch in OneQuestion:
        if ch not in temp:
            temp.append(ch)
    score = score + points[i] * (n - len(temp) + 1)
print(score)