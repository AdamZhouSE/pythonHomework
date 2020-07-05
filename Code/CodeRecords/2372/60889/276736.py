numOfInput = int(input())
for i in range(numOfInput):
    nxy = input().split(" ")
    n = int(nxy[0])
    x = int(nxy[1])
    y = int(nxy[2])
    Ai = input().split(" ")
    if len(Ai) > n:
        Ai.pop(n)
    Ai = list(map(int,Ai))
    Bi = input().split(" ")
    Bi = list(map(int,Bi))
    summary = 0
    difference = []
    for j in range(n):
        summary = summary + Ai[j]
        difference.append(Bi[j]-Ai[j])
    difference.sort()
    difference.reverse()
    for j in range(len(difference)):
        if difference[j] < 0:
            break
    if j < y:
        j = y
    if j > n -x:
        j = n - x
    for k in range(j):
        summary = summary + difference[k]
    print(summary)