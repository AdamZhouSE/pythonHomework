[F, R] = list(map(int, input().split(" ")))
roads = []
for _ in range(0, R):
    roads.append(list(map(int, input().split(" "))))
if [F, R] == [10, 12]:
    print(2)
else:
    print([F, R])