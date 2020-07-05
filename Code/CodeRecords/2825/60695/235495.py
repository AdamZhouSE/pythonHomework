n = int(input())
scores = [None]*n
total = [None]*n
for i in range(0, n):
    scores[i] = input()
for i in range(0, n):
    s = scores[i].split(" ")
    t = 0
    for j in range(0, 4):
        t = t + int(s[j])
    total[i] = t
result = 1
for i in range(1, n):
    if total[0] < total[i]:
        result += 1
print(result)