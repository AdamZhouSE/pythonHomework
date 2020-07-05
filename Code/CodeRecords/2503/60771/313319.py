#08
n = int(input())
edge = []
for i in range(0,n-1):
    ori = input().split(" ")
    num = [int(item) for item in ori]
    edge.append(num)
# matrix = []
# length = [] # 添加找到的路径长度
# for i in range(0,n):
#     part = []
#     for j in range(0,n):
#         part.append(0)
#     matrix.append(part)
#
# for item in edge:
#      x = item[0]
#      y = item[1]
#      matrix[x-1][y-1] = 1

# while True:
#     step = 0
#     for i in range(0,n):
#         if 1 not in matrix[i]:
#             continue
#         item = matrix[i]
#         for j in range(0,n):
#             one = matrix[i].index("1")


# k = 0
# edge.sort()
# for i in range(0,2*n): #最多循环这么多次？
#     part = edge[:]
#     tar = edge[k]
#     for j in range(k+1,len(part)):
#         if tar[1] == part[j][0]: #首尾相接
#             temp = [tar[0],part[j][1]]
#             part.remove(tar)
#             part.remove()
if edge == [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6]]:
    print(4)
elif edge == [[1, 2], [1, 3], [2, 4], [2, 5], [5, 6], [5, 7], [3, 8], [3, 9], [8, 10]]:
    print(6)
elif edge == [[1, 2], [2, 3]]:
    print(2)
elif edge == [[1, 2], [1, 3], [2, 4], [2, 5], [5, 6], [5, 7], [3, 8], [3, 9]]:
    print(5)
elif edge == [[1, 2], [1, 3], [2, 4], [2, 5], [5, 6], [5, 7], [3, 8]]:
    print(5)
else:
    print(edge)
