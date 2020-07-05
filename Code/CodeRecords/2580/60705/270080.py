m = int(input())
n = int(input())
l = int(input())
moves = []
for i in range(0, l):
    moves.append(list(map(int, input().split(","))))
minx = min(sorted(moves, key=lambda k: k[0])[0][0], m)
miny = min(sorted(moves, key=lambda k: k[1])[0][1], n)
print(minx * miny)