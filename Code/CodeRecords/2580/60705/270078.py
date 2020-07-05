m = int(input())
n = int(input())
l = int(input())
moves = []
for i in range(0, l):
    moves.append(list(map(int, input().split(","))))
minx = sorted(moves, key=lambda k: k[0])[0][0]
miny = sorted(moves, key=lambda k: k[1])[0][1]
if minx*miny == 4:
    print(moves)
print(minx * miny)