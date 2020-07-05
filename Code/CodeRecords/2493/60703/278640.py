n = int(input())
types = [int(x) for x in input().split(" ")]
m = int(input())
res = []
moves = []
for i in range(m):
    l,r = [int(x) for x in input().split(" ")]
    moves.append([l,r])
    rrr = types[l-1:r]
    res.append(len(set(rrr)))

for i in res:
    print(i)    