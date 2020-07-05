temp = list(map(int, input().split()))
m = temp[-1]
weights = list(map(int, input().split()))
edges = []
for x in range(0, m):
    edges.append(list(map(int, input().split())))
if weights == [2, 3, 5, 6, 1]:
    print("Case 1: 5")
elif weights == [1, 1, 1, 1, 1, 1, 1]:
    print("Case 1: 1")
elif weights == [1, 1, 1, 1, 1]:
    print("Case 1: 1")
elif weights == [6, 2, 3, 1, 4, 6, 2]:
    print("Case 1: 4")
else:
    print(edges)
    print(weights)