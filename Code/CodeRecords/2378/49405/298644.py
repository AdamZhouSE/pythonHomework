fat = [i for i in range(101)]
def find(x):
    global fat
    if x == fat[x]: return x
    fat[x] = find(fat[x])
    return fat[x]
def merge(x, y):
    global fat
    fat[find(x)] = find(y)
sum = 0
n, m = map(int, input().split())
e = []
for i in range(m):
    e.append(list(map(int, input().split())))
    sum += e[len(e) - 1][2]
e.sort(key=lambda x: x[2])
cnt = 0
for r in e:
    if find(r[0]) == find(r[1]): continue
    cnt += 1
    merge(r[0], r[1])
    sum -= r[2]
    if cnt == n - 1: break
print(sum, end="")