def distance(point1, point2) -> int:
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

guards = [eval(input()) for _ in range(eval(input()))]
target = eval(input())
dist = distance((0, 0), target)
for point in guards:
    if distance(point, target) <= dist:
        print(False)
        exit()
print(True)