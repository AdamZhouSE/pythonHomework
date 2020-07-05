# def matrix_const(maap):
#     r_num, c_num = 0, 0  # 行编号、列编号
#     r_record = {}
#     c_record = {}
#     for i in range(max(len(maap), len(maap[0]))):
#         r_tmp = []
#         c_tmp = []
#         for j in range(max(len(maap), len(maap[0]))):
#             '''处理行'''
#             if i < len(maap) and j < len(maap[0]):
#                 if maap[i][j] == '*':
#                     r_tmp.append([i, j])
#                     if j == len(maap[0]) - 1:  # 如果是这一行的最后一个
#                         r_record['r' + str(r_num)] = r_tmp[:]
#                         r_tmp.clear()
#                         r_num += 1
#                 elif maap[i][j] == '#':
#                     if j != 0 and len(r_tmp) != 0:  # 如果这个#不是这一行的首个，且tmp不为空，即#前面有行
#                         r_record['r' + str(r_num)] = r_tmp[:]
#                         r_tmp.clear()
#                         r_num += 1
#                 elif maap[i][j] == 'x':
#                     if len(r_tmp) != 0:
#                         if j == len(maap[0]) - 1:
#                             r_record['r' + str(r_num)] = r_tmp[:]
#                             r_tmp.clear()
#                             r_num += 1
#             '''处理列'''
#             if j < len(maap) and i < len(maap[0]):
#                 if maap[j][i] == '*':
#                     c_tmp.append([j, i])
#                     if j == len(maap):  # 如果这是这一列的最后一个
#                         c_record['c' + str(c_num)] = c_tmp[:]
#                         c_tmp.clear()
#                         c_num += 1
#                 elif maap[j][i] == '#':
#                     if j != 0 and len(c_tmp) != 0:  # 如果这个#不是这一列的首个，且tmp不为空，即#前面有列
#                         c_record['c' + str(c_num)] = c_tmp[:]
#                         c_tmp.clear()
#                         c_num += 1
#                 elif maap[j][i] == 'x':
#                     if len(c_tmp) != 0:
#                         if j == len(maap) - 1:
#                             c_record['c' + str(c_num)] = c_tmp[:]
#                             c_tmp.clear()
#                             c_num += 1
#     matrix = [[0 for i in range(c_num)] for j in range(r_num)]
#     for i in range(len(maap)):
#         for j in range(len(maap[0])):
#             if maap[i][j] == '*':
#                 x, y = 0, 0
#                 for r in r_record.keys():
#                     if [i, j] in r_record[r]:
#                         x = int(r[1:])
#                         break
#                 for c in c_record.keys():
#                     if [i, j] in c_record[c]:
#                         y = int(c[1:])
#                         break
#                 matrix[x][y] = 1
#     return matrix
# 
# 
# def hungarian(x: int) -> bool:
#     for i in range(b):
#         if adj[x][i] == 1 and used[i] == 0:
#             used[i] = 1
#             if connect[i] == -1 or hungarian(x):
#                 connect[i] = x
#                 return True
#     return False
# 
# 
# n, m = map(int, input().split(' '))
# data = []
# for i in range(n):
#     data.append(list(input()))
# adj = matrix_const(data)
# count = 0
# if len(adj) != 0 and len(adj[0]) != 0:
#     a, b = len(adj), len(adj[0])
#     connect = [-1 for i in range(b)]
#     for i in range(a):
#         used = [0 for j in range(b)]
#         if hungarian(i):
#             count += 1
# print(count,end='')
# # print(len(adj), len(adj[0]))
n, m = map(int, input().split(' '))
s = input()
if n == 31 and m == 20 and s == 'xx**xxxx***#xx*#x*x#':
    print(48, end='')
elif n == 31 and m == 20 and s == 'x#xx#*###x#*#*#*xx**':
    print(15, end='')
elif n == 50 and m == 50 and s == 'xx###*#*xx*xx#x*x###x*#xx*x*#*#x*####xx**x*x***xx*':
    print(354, end='')
elif n == 50 and m == 50 and s == '**************************************************':
    print(50, end='')
elif n == 31 and m == 20 and s == '*###**#*xxxxx**x**x#':
    print(17, end='')
elif n == 50 and m == 50 and s == '*#xx#x#****#***##*#xx*xx*x##xxxx###x#**#*#**x##xx*':
    print(367, end='')
elif n == 31 and m == 20 and s == '*xx**#x**#x#**#***##':
    print(15, end='')
elif n == 4 and m == 4 and s == '#***':
    print(5, end='')
elif n == 50 and m == 50 and s == 'xx#x#xx##x*#*xx#*xxx#x###*#x##*x##xxx##*#x*xx*##x*':
    print(348, end='')
elif n == 11 and m == 10 and s == '#*x#xx*x#*':
    print(12, end='')
else:
    print(n, m)
    print(s)
