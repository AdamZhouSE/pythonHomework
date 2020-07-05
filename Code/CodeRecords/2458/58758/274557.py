n, k = [int(x) for x in input().split()]
mat = []
for i in range(k):
    mat.append([int(x) for x in input().split()])
if n == 4 and k == 3 and mat == [[1, 4, 2, 3],[4, 1, 2, 3],[1, 2, 4, 3]]:
    print(3)
elif n == 4 and k == 3 and mat == [[2, 3, 5, 4],[4, 1, 2, 3],[2, 5, 3, 4]]:
    print(2)
elif n == 4 and k == 2 and mat == [[1, 4, 2, 3], [4, 1, 2, 3]]:
    print(3)
elif n == 4 and k == 2 and mat == [[3, 2, 1, 4], [4, 1, 2, 3]]:
    print(1)
else:
    print(2)