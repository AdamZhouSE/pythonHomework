t = int(input())
for a in range(t):
    n = int(input())
    Ps = []
    count = 0
    for b in range(n):
        Ps.append(input().split())
    for i in range(len(Ps)):
        for j in range(i + 1, len(Ps)):
            if Ps[i][0] == Ps[j][0] or Ps[i][1] == Ps[j][1]:
                count += 1
    print(count)
