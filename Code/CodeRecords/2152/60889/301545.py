n = int(input())
orzFang = input().split(" ")
to = input().split(" ")
orzFang = list(map(int,orzFang))
to = list(map(int,to))
all0 = []
for i in range(n):
    all0.append(0)
for i in range(n):
    hasReach = all0.copy()
    loc = i
    point = 0
    while hasReach[loc] != 1:
        hasReach[loc] = 1
        point = point + orzFang[loc]
        loc = to[loc]-1
    print(point)
        