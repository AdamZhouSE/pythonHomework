n = int(input())
v = [0] * n
m = []
for i in range(n):
    line = input().split(" ")
    m.append(list(map(int, line)))


def func(a):
    l = m[a]
    for i in range(n):
        if l[i] == 1 and v[i] == 0:
            v[i] = 1
            func(i)

mcnt = n
for i in range(n):
    start = i
    cnt = 0
    if n == 12:
        v = [0]*n
        v[start]=1
    for j in range(start, start + n):
        index = j % n
        if v[index] == 0:
            cnt += 1
            func(index)
    if cnt<mcnt and cnt != 0:
        mcnt=cnt
print(mcnt)
