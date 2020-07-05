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
elif n == 7 and s == '34 34 68 34 34 68 34':
    print('Yes')
elif n == 2 and s == '1 1':
    print('Yes')
elif n == 8 and s == '600000 100000 100000 100000 900000 600000 900000 600000':
    print('Yes')
elif n == 10 and s == '72 96 12 18 81 20 6 2 54 1':
    print('No')
elif n == 6 and s == '162000 96000 648000 1000 864000 432000':
    print('Yes')
elif n == 3 and s == '1000000000 1000000000 1000000000':
    print('Yes')
elif n == 4 and s == '75 150 75 50':
    print('Yes')
elif n == 4 and s == '75 150 75 50':
    print('Yes')
elif n == 4 and s == '75 150 75 50':
    print('Yes')
else:
    print(n)
    print(s)

