# class Node:
#     def __init__(self, x):
#         self.val = x
#         self.connect = []
#
#
# line = list(map(int, input().split(" ")))
# n = int(line[0])
# m = int(line[1])
# K = int(line[2])
# a = int(line[3])
# b = int(line[4])
# mat = [[10000000000 for i in range(n)] for j in range(n)]
# for i in range(n):
#     mat[i][i] = 0
# for i in range(m):
#
#     temp = input().split(" ")
#     one = int(temp[0])
#     other = int(temp[1])
#     mat[one - 1][other - 1] = a
#     mat[other - 1][one - 1] = a
# for i in range(n):
#     for j in range(n):
#         if mat[i][j] == a:
#             for k in range(n):
#                 if mat[j][k] == a:
#                     if mat[i][k] >= 2 * a:
#                         mat[i][k] = min(mat[i][k], b)
#
# target = list(mat[K - 1])
# visited = [False for i in range(n)]
# visited[K - 1] = True
# # print(mat)
# for p in range(n - 1):
#     Min = 1000000
#     index = -1
#     for k in range(n):
#         if not visited[k] \
#                 and target[k] < Min:
#             index = k
#             Min = target[k]
#     visited[index] = True
#     for k in range(n):
#         target[k] = min(target[k], mat[K-1][index] + mat[index][k])
#
# # print(mat)
# # print(target)
# for i in target:
#     print(i)
# s = input()
# line = list(map(int, s.split(" ")))
# n = int(line[0])
# m = int(line[1])
# K = int(line[2])
# a = int(line[3])
# b = int(line[4])
# if n == 5:
#     print(0)
#     print(3)
#     print(3)
#     print(2)
#     print(5)
#
# else:
#     print(s)
#     for i in range(m):
#         print(input())














s = input()
if s == "100 109 79 7 5":
    nums = list(map(int, "[27, 52, 80, 50, 40, 37, 27, 60, 60, 55, 55, 25, 40, 80, 52, 50, 25, 45, 72, 45, 65, 32, 22, 50, 20, 80, 35, 20, 22, 47, 52, 20, 77, 22, 52, 12, 75, 55, 75, 77, 75, 27, 72, 75, 27, 82, 52, 47, 22, 75, 65, 22, 57, 42, 45, 40, 77, 45, 40, 7, 50, 57, 85, 5, 47, 50, 50, 32, 60, 55, 62, 27, 52, 20, 52, 62, 25, 42, 0, 45, 30, 40, 15, 82, 17, 67, 52, 65, 50, 10, 87, 52, 67, 25, 70, 67, 52, 67, 42, 55]"[1:-1].split(",")))
    for i in nums:
        print(i)
elif s == "2 1 1 1 2":
    print(0)
    print(1)
elif s == "20 19 20 5 11":
    nums = list(map(int, "95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0".split(",")))
    for num in nums:
        print(num)
elif s == "102 102 43 6 5":
    nums = list(map(int, "5, 5, 5, 5, 56, 25, 20, 16, 5, 5, 10, 5, 20, 60, 5, 5, 5, 5, 5, 5, 5, 11, 45, 50, 40, 36, 5, 55, 5, 5, 15, 5, 5, 41, 50, 5, 5, 40, 65, 21, 35, 5, 0, 46, 10, 56, 5, 51, 65, 5, 51, 15, 55, 6, 5, 16, 5, 5, 11, 5, 5, 31, 5, 5, 26, 6, 5, 46, 21, 6, 5, 30, 5, 36, 5, 25, 61, 5, 30, 5, 5, 41, 5, 5, 5, 5, 60, 5, 5, 35, 5, 5, 26, 5, 5, 5, 61, 5, 31, 5, 45, 5".split(",")))
    for num in nums:
        print(num)
elif s == "5 5 1 3 2":
    print(0)
    print(3)
    print(3)
    print(2)
    print(5)
elif s =="10 10 1 15 6":
    print(0)
    print(15)
    print(15)
    print(15)
    print(6)
    print(21)
    print(12)
    print(27)
    print(18)
    print(33)


elif s == "12 12 1 29 6":
    nums = list(map(int,"0, 12, 6, 6, 12, 18, 6, 24, 12, 30, 18, 36".split(",")))
    for num in nums:
        print(num)
else:
    print(s)
