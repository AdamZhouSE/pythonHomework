d = [4, 7]
i = 0
while len(d) < 2000:
    x = str(d[i])
    d.append(int(x + '4'))
    d.append(int(x + '7'))
    i += 1
d.sort()

T = int(input())
for t in range(T):
    x = int(input())
    print(d[x - 1])