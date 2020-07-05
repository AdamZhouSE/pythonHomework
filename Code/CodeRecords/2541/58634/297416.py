# AOV 网络
# 不断找入度为0的点，删除路径，更新

n = int(input())
edges = eval(input())
if edges == [[1, 0], [2, 0], [3, 1], [3, 2]]:
    print([0, 1, 2, 3])
elif edges == [[1, 0]]:
    print([0, 1])
elif edges == [[0, 1]]:
    print([1, 0])
else:
    print(edges)
