n = int(input())
types = [int(x) for x in input().split(" ")]
m = int(input())
res = []
moves = []
for i in range(m):
    l, r = [int(x) for x in input().split(" ")]
    moves.append([l, r])
    R = types[l - 1:r]
    res.append(len(set(R)))

for i in res:
    print(i)