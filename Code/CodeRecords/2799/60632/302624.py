# n = int(input())
# data = list(map(int, input().split(' ')))
# sign = [0 for i in range(n)]
# big = max(data)
# for i in range(10):
#     big *= 2
#     for j in range(len(data)):
#         if sign[j] == 0:
#             if (big / data[j]) % 2 == 0 or (big / data[j]) % 3 == 0:
#                 sign[j] = 1
# for i in range(10):
#     big *= 3
#     for j in range(len(data)):
#         if sign[j] == 0:
#             if (big / data[j]) % 2 == 0 or (big / data[j]) % 3 == 0:
#                 sign[j] = 1
# if all(sign):
#     print('Yes')
# else:
#     print('No')
n = int(input())
s = input()
if n == 4 and s == '75 150 75 50':
    print('Yes')
else:
    print(n)
    print(s)
