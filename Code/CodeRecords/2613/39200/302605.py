t = int(input())
N = []
for x in range(t):
    N.append(int(input()))
maxN = max(N)
Connell = [1]
count = 2
while len(Connell) < maxN:
    Connell.append(Connell[len(Connell) - 1] + 1)
    while len(Connell) < count * (count+1) / 2:
        Connell.append(Connell[len(Connell) - 1] + 2)
    count += 1
for x in N:
    for i in range(x):
        if i == x - 1:
            print(Connell[i])
        else:
            print(Connell[i], end=" ")
